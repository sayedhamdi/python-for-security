import socket
for port in range (50000):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   result = sock.connect(('142.251.37.193',port))
   if result == 0:
      print ("Port is open")
      sock.close()
   else:
      print ("Port is not open")
      sock.close()
