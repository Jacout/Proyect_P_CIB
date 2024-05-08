from fpdf import FPDF

class PDF(FPDF):
    pass    

    def texts(self, name):
        with open(name, 'rb') as xy:
            txt = xy.read().decode('latin-1')
        self.set_xy(10.0, 40.0)
        self.set_text_color(0, 0, 0)  
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, txt)

    def add_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 0, 0)  
        title_width = self.get_string_width(title)
        self.set_xy((210 - title_width) / 2, 10)
        self.cell(w=title_width, h=10, align='C', txt=title, border=1)




def crear(archivo):
    pdf = PDF()
    pdf.add_page()
    pdf.texts(archivo) #AQUI VA EL TXT QUE SE VA A CONVERTIR A PDF
    pdf.add_title(archivo) #NOMBRE DEL PDF
    pdf.set_author('Bystec') #NOMBRE DEL AUTOR
    pdf.output(f'Reportes/{archivo}.pdf','F') #NOMBRE DEL 