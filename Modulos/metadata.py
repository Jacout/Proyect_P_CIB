import PyPDF2
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os


def readPDF(path):
    #Leer PDF y extraer info
    pdf = open(path, "rb") #En esta variable se asigna el nombre del pdf que se va a utilizar
    reader = PyPDF2.PdfReader(pdf)
    meta = reader.metadata
    if os.path.exists('Reportes\r_metadatos_pdf.txt'):
        f = open('reportes/meta_pdf.txt','a')
        f.write("Autor: ",meta.author)
        f.write("Creador: ",meta.creator)
        f.write("Producido: ",meta.producer)
        f.write(meta.subject)
        f.write("Titulo: ",meta.title)
        f.close()
    else:
        f = open('reportes/meta_pdf.txt','w')
        f.write("Autor: ",meta.author)
        f.write("Creador: ",meta.creator)
        f.write("Producido: ",meta.producer)
        f.write(meta.subject)
        f.write("Titulo: ",meta.title)
        f.close()


#PONER METADATOS PARA FOTOS
class metaimg():
    # -*- encoding: utf-8 -*-

    def decode_gps_info(exif):
        gpsinfo = {}
        if 'GPSInfo' in exif:
        #Parse geo references.
            Nsec = exif['GPSInfo'][2][2] 
            Nmin = exif['GPSInfo'][2][1]
            Ndeg = exif['GPSInfo'][2][0]
            Wsec = exif['GPSInfo'][4][2]
            Wmin = exif['GPSInfo'][4][1]
            Wdeg = exif['GPSInfo'][4][0]
            if exif['GPSInfo'][1] == 'N':
                Nmult = 1
            else:
                Nmult = -1
            if exif['GPSInfo'][1] == 'E':
                Wmult = 1
            else:
                Wmult = -1
            Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
            Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
            exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

 
    def get_exif_metadata(image_path):
        ret = {}
        image = Image.open(image_path)
        if hasattr(image, '_getexif'):
            exifinfo = image._getexif()
            if exifinfo is not None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
        decode_gps_info(ret)
        return ret
    
    def saveMeta(ruta):
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                print(os.path.join(root, name))
                print ("[+] Metadata for file: %s " %(name))
                try:
                    exifData = {}
                    exif = get_exif_metadata(name)
                    for metadata in exif:
                        if os.path.exists('Reportes\r_metadatos_imagenes.txt'):
                            fimg = open('Reportes\r_metadatos_imagenes.txt','a')
                            fimg.write('Metadata: %s - Value: %s ' %(metadata,exif[metadata]))
                            fimg.write('\n')
                            fimg.close()
                        else:
                            fimg = open('Reportes\r_metadatos_imagenes.txt','w')
                            fimg.write('Metadata: %s - Value: %s ' %(metadata,exif[metadata]))
                            fimg.write('\n')
                            fimg.close()
                except:
                    import sys, traceback
                    traceback.print_exc(file=sys.stdout)

def obtenerimg(ruta):
    m = metaimg()
    m.saveMeta(ruta)