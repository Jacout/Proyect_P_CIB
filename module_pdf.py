from PyPDF2 import PdfReader

#parte de pipy
reader = PdfReader("libros\\Python para todos.pdf")
number_of_pages = len(reader.pages)
print("Numero de paginas: ", number_of_pages)
page = reader.pages[40]
text = page.extract_text()
print("Texto",text)

meta = reader.metadata
print("Autor: ",meta.author)
print("Creador: ",meta.creator)
print("Producido: ",meta.producer)
print(meta.subject)
print("Titulo: ",meta.title) #la nueva forma de traer el titulo por los metadatos

#script 
"""
pdfFileObj = open('libros\Python para todos.pdf','rb')
pdf = PdfFileReader(pdfFileObj)
print("Paginas: ", pdf.getNumPages())
print("Titulos: ", pdf.documentInfo.Title)
primera_hoja = pdf.getPage(0)
print(primera_hoja.extractText())
"""