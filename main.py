import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-p","-process", dest="tarea", type=str, choices=[], help="accion a realizar") #SE DEFINE EL PROCESO A REALIZAR
    # Definir el primer argumento que se puede usar para realizar 5 acciones
    parser.add_argument('-a', '--acción', type=str, help='Elegir una de las 5 acciones para realizar')

    # Definir los otros 5 argumentos que se pueden usar para realizar algunas o solo una acción
    parser.add_argument('-w', '--webscraping', type=int, help='Argumento para realizar web scraping')
    parser.add_argument('-i', '--ip', type=str, help='Argumento para escanear puertos e ip')
    parser.add_argument('-m', '--metadatos', type=float, help='Argumento para acción3')
    parser.add_argument('-e', '--arg4', type=bool, help='Argumento para acción4')
    parser.add_argument('-f', '--arg5', type=str, help='Argumento para acción5')
    parser.add_argument("-t","-target", dest="target", help="target")
    args = parser.parse_args()

    
    
    #if (dest  = "all"):
        
        #haga todo
        
        
    
    #web scraping opcional
    #Escaneo de puertos e ip opcional
    #Metadatos opcional si hay documentos o archivos en la pagina en base al web scrapping
    #hash obligatorio, checar si tienen los archivos
    #Virus total en base al chequeo de los correos
    #y api que van a usar dependiendo opcional tambien
    #hacer un argumento de tarea que ejecute solo los que se le indiquen
    
    
    #Si seleccion all ejecute todo
    
    
    import argparse

parser = argparse.ArgumentParser(description='Realizar acciones usando argumentos')


# Realizar acciones basadas en los argumentos proporcionados
if args.acción == 'acción1':
    print(f'Realizando acción1 con argumento {args.arg1}')
elif args.acción == 'acción2':
    print(f'Realizando acción2 con argumento {args.arg2}')
elif args.acción == 'acción3':
    print(f'Realizando acción3 con argumento {args.arg3}')
elif args.acción == 'acción4':
    print(f'Realizando acción4 con argumento {args.arg4}')
elif args.acción == 'acción5':
    print(f'Realizando acción5 con argumento {args.arg5}')
else:
    print('No se especificó ninguna acción. Por favor, proporcione una acción usando la opción -a o --acción.')