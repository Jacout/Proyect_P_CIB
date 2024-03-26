import argparse
import socket
import sys
import openpyxl

def checkPuertosSocket(ip,portlist):
    print("IP",ip,type(ip))
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print ("Puerto {}: \t Abierto".format(port))
            else:
                print ("Puerto {}: \t Cerrado".format(port))
            sock.close()
    except socket.error as error:
        print (str(error))
        print ("Error de conexion")
        sys.exit()



if __name__ == "__main__":
    
    description = """Ejemplo de uso:
        + Escaneo basico:
            -target 127.0.0.1
        + Indica un puerto especifico:
            -target 127.0.0.1 -port 21
        + Indica una lista de puertos:
            -target 127.0.0.1 -port 21,22"""
    parser = argparse.ArgumentParser(description='Port Scanning', epilog=description, #Contructor (empieza con mayuscula) para dar argumentos para dar descripcion del script y sus parametros
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument("-target", metavar='TARGET', dest="target", #Parametro de target
                        help="target to scan", required=True)
    parser.add_argument("-ports", dest="ports", #Parametro de puertos con valor de default
                        help="Please specify the target ports separated by coma[80,8080 by default]", 
                        default = "80,8080")
    params = parser.parse_args() #agrega los parametros
    portlist = params.ports.split(',')#crea una lista con los puertos con split
    puerto = params.target.split()[0]
    print(params)
    for i in range(len(portlist)): #itera, imprime y separa los puertos en enteros
        print("Puerto:", portlist[i])
        portlist[i] = int(portlist[i])
    print(params)
    checkPuertosSocket(puerto,portlist)