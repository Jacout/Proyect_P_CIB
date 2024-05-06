import argparse
import Modulos.portsv2 as portsv2
import Modulos.Scraping as scrap
import Modulos.mod_beatifulsoup_pdf as pdf
import Modulos.mod_beatifulsoup_img as img
if __name__ == "__main__":
    descripcion = """EJEMPLOS DE USO
        + Realizacion de todas las tareas
        -accion all -objetivo <sitio web>
        + Realizacion de solo una tarea especificadas
        -accion web_scrapping -objetivo <sitio web>
        + Realizacion de algunas tareas especificadas:
        -accion web_scrapping,escaneo_puertos,metadatos -objetivo <sitio web>
        Procesos disponibles:
        web_scraping 
        escaneo_puertos 
        metadatos 
        hash 
        correos
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
        print("Realizando todas las acciones")
    else:
        acciones_especificas = args.acciones.split(",")
        
        #accion web_scrapping escaneo_puertos metadatos hash correos api
        for accion in acciones_especificas:
            if accion == "web_scraping":
                pdf.scrapingPDF(args.objetivo)
                img.descargar_imagenes(args.objetivo)
            if accion == "escaneo_puertos":
                portsv2.escaneo(args.objetivo,puertos)
            if accion == "metadatos":
                print("Realizar metadatos de archivos , verificando si hay archivos")
            if accion == "hash":
                print("Realizar sacar el valor hash de los archivos de descarga como los generados por reportes")
            if accion == "correos":
                print("Consulta Virus total")
            if accion == "api":
                print("Accion a realizar con las API")
                
    #en base a la informacion recolectada se realizan los reportes
    #se manda a llamar a los modulos de generacion de reportes
    #se exporta la informacion en una carpeta de este proyecto
    print("Objetivo:", args.objetivo)
        
    
    #web scraping opcional
    #Escaneo de puertos e ip opcional
    #Metadatos opcional si hay documentos o archivos en la pagina en base al web scrapping
    #hash obligatorio, checar si tienen los archivos
    #Virus total en base al chequeo de los correos
    #y api que van a usar dependiendo opcional tambien
    
    
    #Si seleccion all ejecute todo