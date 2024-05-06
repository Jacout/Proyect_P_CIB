import os
import requests
from bs4 import BeautifulSoup

def scrapingLinks(url):
    print("\nObteniendo links de la url:"+ url)

    try:
        response = requests.get(url)
        parsed_body = BeautifulSoup(response.text, 'html.parser')

        # expresion regular para obtener links
        links = parsed_body.find_all('a', href=True)

        print('Encontrados %s links' % len(links))

        # limpia el txt
        if os.path.exists('Reportes/links.txt'):
            open('Reportes/links.txt', 'w').close()

        # guarda los links pa 
        with open('Reportes/links.txt', 'a') as f:
            for link in links:
                f.write(link['href'] + '\n')

    except Exception as e:
        print(e)
        print("Error conexion con " + url)
        pass

<<<<<<< HEAD
<<<<<<< HEAD
# Llamar a la función con la URL deseada
scrapingLinks("pruba")
=======
# Llamar a la función con la URL deseada
>>>>>>> origin/argparse
=======
# Llamar a la función con la URL deseada

def encabezdos(url):
        r = requests.get(url)
        if r.status_code != 204:
            tipo = r.headers['content-type']
            #guardarlo en un archivo de texto
            with open("Reportes/respuesta.txt", "w", encoding="utf-8") as f:
                f.write(tipo)
>>>>>>> origin/argparse
