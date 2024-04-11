import nmap

# take the range of porst to
# be sccaned

begin = 78
end = 80

# asssing the target ip to be scanned to
# a variable
target = '148.234.5.206'

# instantiate a PortScanner object
scanner = nmap.PortScanner()

for i in range(begin,end+1):
    
    # scan the target 
    res = scanner.scan(target,str(i))
    
    # the result is a dictionary containing
    # several informacion we only need to
    # check if the port is opened or closed
    res = res['scan'][target]['tcp'][i]['state']
    
    print(f'port {i} is {res}')