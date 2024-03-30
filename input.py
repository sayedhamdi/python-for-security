ips = []

while True: 
    ip = str(input("give me an ip : "))
    if (ip =="end"):
        for i in ips :
            print(i)
        break
    ips.append(ip+":80")
    
print(ip)


l = [1,3,4]

for number in l : 
    if number ==2:
        print("l9it el two")
        break
