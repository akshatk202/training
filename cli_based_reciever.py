import socket                               # used to send mesage using across network
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)                   # DGRAM= it is the mediam to send message or data
    ip_address= '192.168.147.149'
    port=3310
    complete_add=(ip_address,port)
    s.bind(complete_add)
    while True:
        message = s.recvfrom(120)                   # 120 is data limit
        print(message)
        data = message[0]
        data = '\n'
        print(data.encode('ascii'))
except Exception as e:
    print("hello sir message recieve kr liya hai")