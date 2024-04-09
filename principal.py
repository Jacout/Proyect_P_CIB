import requests

if __name__ == "__main__":
    #buscar 
    #mod_reques()
    
    print("Menu")
    url = input("Ingree una URL")
    r = requests.get(url)
    print(r.status_code)
    if r.status_code != 204:
        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)
        print(r.json)
        #guardarlo en un archivo de texto
        with open("respuesta.html", "w", encoding="utf-8") as f:
            f.write(r.text)
    
    
#modulos realizar busqueda httts -> json contenido de pagina-> checar emails -> web scrapping -> descargar
# checar imagenes y documentos metadatos