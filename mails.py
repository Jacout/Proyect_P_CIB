import requests
import re

url = 'https://www.themoscowtimes.com/page/moscow-times'

response = requests.get(url)
if response.status_code != 200:
    exit()

# a set of crawled emails
regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
new_emails = set(re.findall(regExMail, response.text, re.I))

file = open("correos.txt","w")
for i in new_emails:
    file.write(i + "\n")