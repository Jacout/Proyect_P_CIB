import os
import requests
from lxml import html
from bs4 import BeautifulSoup

def scrapingPDF(url):
    print("\nObteniendo pdfs de la url: " + url)

    try:
        response = requests.get(url)
        parsed_body = html.fromstring(response.text)

        # expresion regular para obtener pdf
        pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')

        # create directory for save pdfs
        if len(pdfs) > 0:
            if not os.path.exists('pdfs'):
                os.makedirs('pdfs')

        print('Encontrados %s pdf' % len(pdfs))

        for pdf in pdfs:
            if pdf.startswith("http") == False:
                download = url + pdf
            else:
                download = pdf
            print(download)

            # descarga pdfs
            r = requests.get(download)
            with open('pdfs/' + os.path.basename(download), 'wb') as f:
                f.write(r.content)

    except Exception as e:
        print(e)
        print("Error conexion con " + url)
        pass

# Llamar a la función con la URL deseada
scrapingPDF("prueba")