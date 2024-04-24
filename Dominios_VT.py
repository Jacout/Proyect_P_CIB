import requests
import api_keys


#Cambiar a url
def get_domain_report(domain):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {"accept": "application/json", "x-apikey": api_keys.api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def is_domain_safe(domain):
    report = get_domain_report(domain)
    if report:
        attributes = report['data']['attributes']
        if attributes['last_analysis_stats']['malicious'] == 0:
            return True
    return False

domain = 'uanl.mx'
if is_domain_safe(domain):
    print(f'El dominio {domain} es seguro.')
else:
    print(f'El dominio {domain} puede no ser seguro.')