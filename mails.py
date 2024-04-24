import requests
import re
def mails():
    response = requests.get(target)
    if response.status_code != 200:
        exit()
#obtiene las urls
    regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
    correos = set(re.findall(regExMail, response.text, re.I))

    file = open("correos.txt","w")
    for i in correos:
        file.write(i + "\n")
     
    file.close()
    