
"""ips = ["192.168.1.1:443","192.168.1.2:80","192.168.1.4:80"]

list_of_fresh_ips = []
for ip in ips : 
    ip_without_port = ip.split(":")[0]
    list_of_fresh_ips.append(ip_without_port)

print(list_of_fresh_ips)

"""


ips = ["192.168.1.1","192.168.1.2","192.168.1.4"]
PORT = 443
new_ips = []
for ip in ips : 
    ip = ip + ":"+str(PORT)
    new_ips.append(ip)

print(new_ips)

