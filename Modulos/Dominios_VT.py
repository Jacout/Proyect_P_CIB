import requests
import os
from datetime import datetime
#Cambios para realizar: Hacer que se guarde en un archivo txt, la fecha, hora, el dominio y la respusta del dominio(24/04/2024)
#Api consumida de VT, apiket guardad en un archivo de python
def get_domain_report(domain):
    try:
        url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        with open('API_Keys/api.key','r') as f:
            api_keys = f.read()
        headers = {"accept": "application/json", "x-apikey": api_keys}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            if os.path.exists('Reportes/r_logs_api.txt'):
                with open('Reportes/r_logs_api.txt','a') as fa:
                    fa.write(f"Error: {response.status_code}")
            else:
                with open('Reportes/r_logs_api.txt','w') as fa:
                    fa.write(f"Error: {response.status_code}")
            return None
    except Exception as e:
        if os.path.exists('Reportes/r_logs_api.txt'):
            with open('Reportes/r_logs_api.txt','a') as fa:
                fa.write(e)
        else:
            with open('Reportes/r_logs_api.txt','w') as fa:
                fa.write(e)
        
#Utilizamos los parametros que nos brinda VT para verificar si el dominio es seguro o malicioso
def is_domain_safe(domain):
    try:
        report = get_domain_report(domain)
        if report:
            attributes = report['data']['attributes']
            if attributes['last_analysis_stats']['malicious'] == 0:
                return True
        return False
    except Exception as e:
        if os.path.exists('Reportes/r_logs_api.txt'):
            with open('Reportes/r_logs_api.txt','a') as fa:
                fa.write(e)
        else:
            with open('Reportes/r_logs_api.txt','w') as fa:
                fa.write(e)


#Prueba con dominio no seguro
#Para dominio seguro puedes probar con el de uanl.mx

def checar_dom(url):
    ahora = datetime.now()
    
    fecha = ahora.strftime("%Y%m%d_%H%M%S")
    if is_domain_safe(url):
        if os.path.exists(f'Consulta_API/consulta_{fecha}.txt'):            
            with open(f'Consulta_API/consulta_{fecha}.txt','a') as fa:
                fa.write(f'El dominio {url} es seguro')
        else:
            with open(f'Consulta_API/consulta_{fecha}.txt','w') as fa:
                fa.write(f'El dominio {url} es seguro')
    else:
        if os.path.exists(f'Consulta_API/consulta_{fecha}.txt'):
            with open(f'Consulta_API/consulta_{fecha}.txt','a') as fa:
                fa.write(f'El dominio {url} puede no ser seguro')
        else:
            with open(f'Consulta_API/consulta_{fecha}.txt','w') as fa:
                fa.write(f'El dominio {url} puede no ser seguro')
