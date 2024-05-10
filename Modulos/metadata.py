import PyPDF2
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os


def readPDF(path):
    #Leer PDF y extraer info
    try:
        pdf = open(path, "rb") #En esta variable se asigna el nombre del pdf que se va a utilizar
        reader = PyPDF2.PdfReader(pdf)
        meta = reader.metadata
        print(meta)
        if  os.path.exists('Reportes\r_meta_pdf.txt'):
            with open('Reportes/r_meta_pdf.txt','a') as f:
                f.write("Autor: " + str(meta.author))
                f.write("Creador: " + str(meta.creator))
                f.write("Producido: " + str(meta.producer))
                f.write(str(meta.subject))
                f.write("Titulo: " + str(meta.title))
            
        else:
            with open('Reportes/r_meta_pdf.txt','w') as f:
                f.write("Autor: " + str(meta.author))
                f.write("Creador: " + str(meta.creator))
                f.write("Producido: " + str(meta.producer))
                f.write(str(meta.subject))
                f.write("Titulo: " + str(meta.title))
    except Exception as e:
            if os.path.exists('Reportes/r_logs_pdf.txt'):
                with open('Reportes/r_logs_pdf.txt','a') as fw:
                    fw.write('Exception: \n' + str(e))
            else:
                with open('Reportes/r_logs_pdf.txt','w') as fw:
                    fw.write('Exception: \n' + str(e))


class metaimg():
    def decode_gps_info(self, exif):
        gpsinfo = {}
        try: 
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
        except Exception as e:
            if os.path.exists('Reportes/r_logs_meta.txt'):
                with open('Reportes/r_logs_meta.txt','a') as fw:
                    fw.write('Exception: \n' + str(e))
            else:
                with open('Reportes/r_logs_meta.txt','w') as fw:
                    fw.write('Exception: \n' + str(e))
        return exif
    
    def get_exif_metadata(self,image_path):
        ret = {}
        try:    
            image = Image.open(image_path)
            if hasattr(image, '_getexif'):
                exifinfo = image._getexif()
                if exifinfo is not None:
                    for tag, value in exifinfo.items():
                        decoded = TAGS.get(tag, tag)
                        ret[decoded] = value
            self.decode_gps_info(ret)
            return ret
        except Exception as e:
            if os.path.exists('Reportes/r_logs_meta.txt'):
                with open('Reportes/r_logs_meta.txt','a') as fw:
                    fw.write('Exception: \n' + str(e))
            else:
                with open('Reportes/r_logs_meta.txt','w') as fw:
                    fw.write('Exception: \n' + str(e))
    
    def saveMeta(self,ruta):
        try:
            for root, dirs, files in os.walk(".", topdown=False):
                for name in files:
                    print(os.path.join(root, name))
                    print ("[+] Metadata for file: %s " %(name))
                    try:
                        exifData = {}
                        exif = self.get_exif_metadata(name)
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
                    except Exception as e:
                        import sys, traceback
                        if os.path.exists('Reportes/r_logs_meta.txt'):
                            with open('Reportes/r_logs_meta.txt','a') as fw:
                                fw.write('Exception: \n' + str(e) + str(file=sys.stdout))
                        else:
                            with open('Reportes/r_logs_meta.txt','w') as fw:
                                fw.write('Exception: \n' + str(e) + str(file=sys.stdout))
                        import sys, traceback
                        traceback.print_exc(file=sys.stdout)
        except  Exception as e:
            if os.path.exists('Reportes/r_logs_meta.txt'):
                with open('Reportes/r_logs_meta.txt','a') as fw:
                    fw.write('Exception: \n' + str(e))
            else: 
                with open('Reportes/r_logs_pdf.txt','w') as fw: 
                    fw.write('Exception: \n' + str(e))
                pass
