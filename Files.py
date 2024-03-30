
#open a file and store it in a variable
file = open("ips.txt","r")
PORT = "443"
#use a method of reading the file
ips_with_ports = []
ips = file.readlines()

for ip in ips:
    ips_with_ports.append(ip + ":" + PORT)

for ip in ips_with_ports :
    new_ip = ip.replace("\n","")
    print(new_ip)
    ips.append(new_ip)
print(ips)
#close the file
file.close()

l = ["ali","hsan","ahmed","selim","kamel","ahmed moshen","taher"]


for name in l:
    print(name)
    print("marhbe")
   

