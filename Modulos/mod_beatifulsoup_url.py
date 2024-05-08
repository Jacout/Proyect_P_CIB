import os
import requests
from bs4 import BeautifulSoup
import re

def scrapingLinks(url):
    try:
        response = requests.get(url)
        parsed_body = BeautifulSoup(response.text, 'html.parser')

        # expresion regular para obtener links
        links = parsed_body.find_all('a', href=True)

        # limpia el txt
        if os.path.exists('Reportes/links.txt'):
            open('Reportes/links.txt', 'w').close()

        # guarda los links pa 
        with open('Reportes/links.txt', 'a') as f:
            for link in links:
                f.write(link['href'] + '\n')

    except Exception as e:
        if os.path.exists('Reportes/r_logs_url.txt'):
                with open('Reportes/r_logs_url.txt','a') as fw:
                    fw.write('Exception: \n' + str(e))
                    fw.write('Error conexion con' + url)
        else:
                with open('Reportes/r_logs_url.txt','w') as fw:
                    fw.write('Exception: \n' + str(e))
                    fw.write('Error conexion con' + url)
        pass

def encabezdos(url):
        r = requests.get(url)
        if r.status_code != 204:
            tipo = r.headers['content-type']
            with open("Reportes/respuesta.txt", "w", encoding="utf-8") as f:
                f.write(tipo)

def mails(target):
    response = requests.get(target)
    if response.status_code != 200:
        if os.path.exists('Reportes/r_logs_url.txt'):
                with open('Reportes/r_logs_url.txt','a') as fw:
                    fw.write('Error de conexion')
        else:
                with open('Reportes/r_logs_url.txt','w') as fw:
                    fw.write('Error de conexion')
        exit()
    
    regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
    new_emails = set(re.findall(regExMail, response.text, re.I))

    with open("Reportes/correos.txt","w") as file:
        for i in new_emails:
            file.write(i + "\n")