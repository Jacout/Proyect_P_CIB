import requests
import re

url = input("Tecla la URL \n")

response = requests.get(url)
if response.status_code !=200:
    exit()
    
    
# a guardar los correos
regexMail = r"[a-z0-9\.\+-_]+@[a-z0-9\.\-+_]+\.[a-z]+"
new_emails = set(re.findall(regexMail,response.text,re.I))
for i in new_emails:
    print(i)