import os
import shutil
import requests
from bs4 import BeautifulSoup
#Crea una clase llamada Scraper
class Scraper:
    def scrapingBeautifulSoup_Imagenes(self, url):
        # Ruta del directorio de imagenes
        images_dir = "images"

        try:
            print("Obteniendo imagenes con BeautifulSoup " + url)

            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'lxml')

            # Verifica si el directorio de imagenes existe y si es asi lo borra 
            if os.path.exists(images_dir):
                self.limpiar_directorio(images_dir)
            else:
                os.makedirs(images_dir)

            for tagImage in bs.find_all("img"): 
                if not tagImage['src'].startswith("http"):
                    download = url + tagImage['src']
                else:
                    download = tagImage['src']
                print(download)
                # Descarga la imagenes y la ingresa en la carpeta images 
                r = requests.get(download)
                if r.status_code == 200:
                    f = open(os.path.join(images_dir, os.path.basename(download)), 'wb')
                    f.write(r.content)
                    f.close()
                else:
                    print("Error al descargar la imagen: " + download)

        except Exception as e:
            print(e)
            print("Error conexion " + url)
            pass

    def limpiar_directorio(self, dir_path):
        # En esta funcion hace que despues de cada petición diferente se eliminen las imagenes de la anterior petición se utulizo la librería shtil
        for filename in os.listdir(dir_path):
            dir_path = os.path.join(dir_path, filename)
            try:
                if os.path.isfile(dir_path) or os.path.islink(dir_path):
                    os.unlink(dir_path)
                elif os.path.isdir(dir_path):
                    shutil.rmtree(dir_path)
            except Exception as e:
                print('Fallo en la eliminación %s. Razon: %s' % (dir_path, e))

def descargar_imagenes():
    Scraper.scrapingBeautifulSoup_Imagenes() #falta agregar lo de valores hash