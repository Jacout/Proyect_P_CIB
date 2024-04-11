#pip install python-whois
#para sacar informacion del dominio
import whois

domain = input()
domain_info = whois.whois(domain)
for key, value in domain_info.items():
    print (key,':',value)
