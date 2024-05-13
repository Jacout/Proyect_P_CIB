import argparse
import os
import Modulos.portsv2 as portsv2
import Modulos.mod_beatifulsoup_img as imagen
import Modulos.mod_beatifulsoup_pdf as pdf
import Modulos.mod_beatifulsoup_url as links
import Modulos.Encriptado_files as enFiles
import Modulos.Crearbase as Hash
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
        api"""
    parser = argparse.ArgumentParser(description='Script para investigacion web',epilog=descripcion,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    # Definir el primer argumento que se puede usar para realizar 5 acciones
    parser.add_argument('-accion', dest='acciones', 
                        type=str, help='Especificar los procesos a realizar [all default]', default= 'all')
    parser.add_argument('-objetivo', dest='objetivo',type=str, help="Sitio objetivo", required=True)
    parser.add_argument("-ports", dest="ports", #Parametro de puertos con valor de default
                        help="Please specify the target ports separated by coma[80,8080 by default]", 
                        default = "80,8080")
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
        portsv2.escaneo(args.objetivo,args.ports)


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
    
    def subdirectorio(ruta): #obtener subdirectorio y mandar solo los folders
        for archivo in os.listdir(ruta):
            """_summary_

            Args:
            ruta (_type_): _description_
            Si es la carpeta .git se ignora
            """
            if os.path.isdir(archivo):
                subdirectorio(archivo)
                ruta = os.path.abspath(archivo)
                Hash.obtener(ruta,archivo)
                
    ruta_raiz = os.getcwd()
    Hash.obtener(ruta_raiz,'Raiz')
    
    subdirectorio(ruta_raiz)
    

    #crear pdf
    ruta_pdf = 'Reportes'
    for archivo in os.listdir(ruta_pdf):
        if archivo.endswith('.txt'):
            archivolimpiar = os.path.join(ruta_pdf,archivo)
            enFiles.encriptacion(archivolimpiar)
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