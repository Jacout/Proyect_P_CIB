from PyPDF2 import PdfFileReader

pdfFileObj = open('libros\fp.pdf','rb')
pdf = PdfFileReader(pdfFileObj)
print("Paginas: ", pdf.getNumPages())
print("Titulos: ", pdf.documentInfo.Title)
primera_hoja = pdf.getPage(0)
print(primera_hoja.extractText())
