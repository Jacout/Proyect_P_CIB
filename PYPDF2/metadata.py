import PyPDF2

#Leer PDF y extraer info
pdf = open("ElPrincipito.pdf", "rb") #En esta variable se asigna el nombre del pdf que se va a utilizar
reader = PyPDF2.PdfReader(pdf)
meta = reader.metadata

#Script para obtener metadatos del pdf y mostrar en consola
print("Autor: ",meta.author)
print("Creador: ",meta.creator)
print("Producido: ",meta.producer)
print(meta.subject)
print("Titulo: ",meta.title)

""" page = reader._get_page(0) #Método para leer información del PDF

info = page.extract_text() #Método para extraer texto del pdf y guardarlo en una variable
print(info) #Muestra en consola el texto extraido

#Método para guardar info en TXT 
with open ("info_pdf.txt", "w") as txt:
    txt.write(info) """

