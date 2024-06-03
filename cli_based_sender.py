# port limit 0 to 65536
# ip_address = 192.168.233.149
# port = 8888

import socket                               # used to send mesage using across network
try:                                        #
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)                   # DGRAM= it is the mediam to send message or data
    ip_address= '192.168.136.174'
    port=8080
    target=(ip_address,port)
    message=input("kya message kroge: ")
    encript_message=message.encode('ascii')
    s.sendto(encript_message,target)
except Exception as e:                      # 
    print("no need")