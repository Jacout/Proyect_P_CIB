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
# Llamar a la función con la URL deseada
scrapingLinks("pruba")
=======
# Llamar a la función con la URL deseada
>>>>>>> origin/argparse
