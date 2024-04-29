import requests
import re

response = requests.get(target)
if response.status_code != 200:
    exit()
#obtiene las urls
regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
new_emails = set(re.findall(regExMail, response.text, re.I))

file = open("correos.txt","w")
for i in new_emails:
    file.write(i + "\n")