#escaneo de puertos
import sys
import socket
from datetime import datetime

def escaneo(target,puertos):
#crea un archivo para ir guaradando la hora de inicio y futura informacion
    hora_inicio= datetime.now()#guarda la hora de inicio del escaneo
    with open("Escaneo de puertos.txt","w") as file:
        file.write(f"Dia y hora de inicio: {hora_inicio}")

#obtiene la direccion ip a escannear aun se necesita el parametro "target" 
#OJO en caso de que target no sea una url/dirreccion valida ocurrira la siguiente exepcion:
    try:
        ip=socket.gethostbyname(target)#obtiene la direccion ip
    except socket.gaierror:
        with open("Error.txt","w") as fileE:
            fileE.write(f"\n El host no existe{hora_inicio}")#guarda el error en el archivo diferente
        sys.exit()

    for port in puertos:
        try:#esta exepcion verifca el tipo de hots que tenemops
        # AF_INET PARA DIRECCIONES IPV4
        # SOCK_STREAM PARA PROTOCOLO TCP
            serv= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serv.bind((ip,port))
        except:
            with open("Escaneo de puertos.txt","a") as file: #va anexando los puertos en el txt
                file.write(f"\nPuerto abierto: {port}")
#Guarda la hora de conclucion del escaneo            
    hora_final = datetime.now()
    with open("Escaneo de puertos.txt","a") as file:
        file.write(f"\nDia y hora de final: {hora_final}") #cuando termina anexa los tiempos
#Guarda el tiempo que tardo el programa
    with open("Escaneo de puertos.txt","a") as file:
        file.write(f"\nTiempo transcurrido: {hora_final-hora_inicio}")
