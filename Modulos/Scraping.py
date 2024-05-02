# -*- encoding: utf-8 -*-
#class for scraping
import requests
import os

import requests
from lxml import html
from bs4 import BeautifulSoup

#import urlparse

class Scraping:
    
    def scrapingBeautifulSoup(self,url):
    
        try:
            print("Obteniendo imagenes con BeautifulSoup "+ url)
            
            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'lxml')
            
            #create directory for save images
            if not os.path.exists("Graficas/images"):
                os.system("mkdir Graficas/images")
            
            for tagImage in bs.find_all("img"): 
                #print(tagImage['src'])
                if tagImage['src'].startswith("http") == False:
                    download = url + tagImage['src']
                else:
                    download = tagImage['src']
                print(download)
                # download images in img directory
                r = requests.get(download)
                f = open('Graficas/images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
        
        except Exception as e:
                print(e)
                print("Error conexion " + url)
                pass
				
    def scrapingImages(self,url):
        print("\nObteniendo imagenes de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener imagenes
            images = parsed_body.xpath('//img/@src')

            print ('Imagenes %s encontradas' % len(images))
    
            #create directory for save images
            #os.system("mkdir images")
    
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print(download)
                # download images in images directory
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
                
        except Exception as e:
                print(e)
                print ("Error conexion con " + url)
                pass
            
    def scrapingPDF(self,url):
        print("\nObteniendo pdfs de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')
    
            #create directory for save pdfs
            if len(pdfs) >0:
                os.system("mkdir Graficas/pdfs")
        
            print ('Encontrados %s pdf' % len(pdfs))
                
            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                print(download)
                    
                # descarga pdfs
                r = requests.get(download)
                f = open('Graficas/pdfs/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
    
        except Exception as e:
            print(e)
            print("Error conexion con " + url)
            pass
    
    def scrapingLinks(self,url):
            print("\nObteniendo links de la url:"+ url)
        
            try:
                response = requests.get(url)  
                parsed_body = html.fromstring(response.text)
    
                # expresion regular para obtener links
                links = parsed_body.xpath('//a/@href')
    
                print('links %s encontrados' % len(links))
                n = 0
    
                for link in links:
                    #checar si existe el archivo txt en la carpeta reportes
                    if os.path.isfile("Reportes/links.txt") == False:
                        f = open("Reportes/links.txt","w")
                        f.write(link)
                        f.close()
                    else :
                        f = open("Reportes/links.txt","a")
                        f.write(link)
                        f.close()
                    
                
            except Exception as e:
                    print(e)
                    print("Error conexion con " + url)
                    pass
    
    def encabezdos(url):
        r = requests.get(url)
        if r.status_code != 204:
            tipo = r.headers['content-type']
            #guardarlo en un archivo de texto
            with open("Reportes/respuesta.txt", "w", encoding="utf-8") as f:
                f.write(tipo)





def obtener(url):#recibe los parametros de main y los manda a llamar a cada uno de las clases
    S = Scraping()
    S.scrapingBeautifulSoup(url)

