#buscar paginas
import os, time, random, datetime, sqlite3, requests

def guardar(enlace):
    conexion = sqlite3.connect("shd3.db")
    cruso = conexion.cursor()
    fecha = datetime.date.strftime('%Y%m%d')
    cruso.execute(f'''CREATE TABLE IF NOT EXISTS datos_{fecha}
                  (enlace text)''')
    conexion.commit()
    cruso.execute(f'INSERT INTO datos_{fecha} values(?)',[enlace])
    conexion.commit()
    conexion.close()

#para peticiones de las url
def peticiones(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            personaje = r.json()
            print(personaje)
            for x,y in personaje.items():
                print(x,"-",y)
        else:
            print("La pagina no existe, bye")
            exit()
    except requests.exceptions.JSONDecodeError as e:
        print(f"fallo en json: {e}")

def peticiones2(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            if r.headers.get('content-type') == 'application/json':
                personaje = r.json()
                for x, y in personaje.items():
                    print(x, "-", y)
            else:
                print("La respuesta no es JSON")
        else:
            print("El servidor respondió con el código {}".format(r.status_code))
            exit()
    except requests.exceptions.JSONDecodeError as e:
        print(f"fallo en json: {e}")

try:
    from googlesearch import search
except ImportError:
    os.system('pip install google')
    #instala el modulo
    exit()


url2 = input("Ingree una URL")


#pa buscar
query = input ("Busqueda")
print("Cagando....")
time.sleep(2)
for enlace in search(query, tld="com", num=20, stop=20, pause=5):
    print(exec,enlace)
    #peticiones(enlace)
    guardar(enlace)
    