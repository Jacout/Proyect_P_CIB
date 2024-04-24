import requests
import api_keys

#Cambios para realizar: Hacer que se guarde en un archivo txt, la fecha, hora, el dominio y la respusta del dominio(24/04/2024)
#Api consumida de VT, apiket guardad en un archivo de python
def get_domain_report(domain):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {"accept": "application/json", "x-apikey": api_keys.api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
#Utilizamos los parametros que nos brinda VT para verificar si el dominio es seguro o malicioso
def is_domain_safe(domain):
    report = get_domain_report(domain)
    if report:
        attributes = report['data']['attributes']
        if attributes['last_analysis_stats']['malicious'] == 0:
            return True
    return False


#Prueba con dominio no seguro
#Para dominio seguro puedes probar con el de uanl.mx
domain = 'vansemexicos.com'
if is_domain_safe(domain):
    print(f'El dominio {domain} es seguro.')
else:
    print(f'El dominio {domain} puede no ser seguro.')
