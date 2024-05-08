import argparse
import os
import Modulos.portsv2 as portsv2
import Modulos.mod_beatifulsoup_img as imagen
import Modulos.mod_beatifulsoup_pdf as pdf
import Modulos.mod_beatifulsoup_url as links
import Modulos.cifradoCesar2 as CesarAr
import Modulos.Encriptado_files as enFiles
import Modulos.PS.CreateBaseline as Hashes
import Modulos.Dominios_VT as api
import Modulos.pdfMaker as pdfcreador

if __name__ == "__main__":
    descripcion = """EJEMPLOS DE USO
        + Realizacion de todas las tareas
        -accion all -objetivo <sitio web>
        + Realizacion de solo una tarea especificadas
        -accion web_scrapping -objetivo <sitio web>
        + Realizacion de algunas tareas especificadas:
        -accion web_scrapping,escaneo_puertos -objetivo <sitio web>
        Procesos disponibles:
        web_scraping 
        escaneo_puertos  
        api
        encriptacion_txt
        encriptacion_files"""
    parser = argparse.ArgumentParser(description='Script para investigacion web',epilog=descripcion,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    # Definir el primer argumento que se puede usar para realizar 5 acciones
    parser.add_argument('-accion', dest='acciones', 
                        type=str, help='Especificar los procesos a realizar [all default]', default= 'all')
    parser.add_argument('-objetivo', dest='objetivo',type=str, help="Sitio objetivo", required=True)
    parser.add_argument("-ports", dest="ports", #Parametro de puertos con valor de default
                        help="Please specify the target ports separated by coma[80,8080 by default]", 
                        default = "80,8080")
    #Argumentos opcionales de encriptacion
    parser.add_argument('-frase', dest='frase', type=str, help="Frase a encriptar")
    parser.add_argument('-path' , dest='path', type=str, help="Archivo a encriptar")
    args = parser.parse_args()
    #los puertos los convierto en lista
    puertos = args.ports.split(",")  
    
    if args.acciones == "all": #si la entrada del parametro es all ejecuta todas las acciones, es decir manda a llamar a los modulos
        imagen.descargar_imagenes(args.objetivo)
        pdf.scrapingPDF(args.objetivo)
        links.scrapingLinks(args.objetivo)
        links.encabezdos(args.objetivo)
        links.mails(args.objetivo)
        api.checar_dom(args.objetivo)


    else:
        acciones_especificas = args.acciones.split(",")
        
        #accion web_scrapping escaneo_puertos metadatos hash correos api
        for accion in acciones_especificas:
            if accion == "web_scraping":
                imagen.descargar_imagenes(args.objetivo)
                pdf.scrapingPDF(args.objetivo)
                links.scrapingLinks(args.objetivo)
                links.encabezdos(args.objetivo)
                links.mails(args.objetivo)
            if accion == "escaneo_puertos":
                portsv2.escaneo(args.objetivo,puertos)
            if accion == "api":
                api.checar_dom(args.objetivo)
            if accion == "encriptacion_txt":
                CesarAr.Encriptar(args.frase)
            if accion == "encriptacion_files":
                enFiles.encriptacion(args.path)
    ruta_raiz = os.getcwd()
    Hashes.sacar_hash(ruta_raiz)

    #crear pdf
    ruta_pdf = 'Reportes'
    for archivo in os.listdir(ruta_pdf):
        if archivo.endswith('.txt'):
            archivolimpiar = os.path.join(ruta_pdf,archivo)
            pdfcreador.crear(archivo,archivolimpiar)
            try:
                if os.path.isfile(archivolimpiar) or os.path.islink(archivolimpiar):
                    os.unlink(archivolimpiar)
            except Exception as e:
                if os.path.exists('Reportes/r_logs_archivos.txt'):
                    with open('Reportes/r_logs_archivos.txt','a') as f:
                        f.write(f'Error al eliminar {archivolimpiar}. Razón: {e}')
                else:
                    with open('Reportes/r_logs_archivos.txt','w') as f:
                        f.write(f'Error al eliminar {archivolimpiar}. Razón: {e}')
        

    #en base a la informacion recolectada se realizan los reportes
    #se manda a llamar a los modulos de generacion de reportes
    #se exporta la informacion en una carpeta de este proyecto
        
    
    #web scraping opcional
    #Escaneo de puertos e ip opcional
    #Metadatos opcional si hay documentos o archivos en la pagina en base al web scrapping
    #hash obligatorio, checar si tienen los archivos
    #Virus total en base al chequeo de los correos
    #y api que van a usar dependiendo opcional tambien
    
    
    #Si seleccion all ejecute todo