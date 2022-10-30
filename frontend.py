import socket

with open('banner.txt') as file:
    print(file.read())
print('WELCOME TO THE 7ru3 h4ck3r ch47')

port = 1337

sock = socket.socket()
sock.connect(('localhost', port))

nick = str(input('Enter your nickname: '))
sock.send(nick.encode(encoding='UTF-8'))
print('Connection is established, u can start chatting')
friend = sock.recv(1024).decode(encoding='UTF-8')

while True:
    req_msg = sock.recv(1024)
    print(req_msg.decode(encoding='UTF-8'))

    msg = str(input('Inp msg: '))
    data = ': '.join([nick, msg])
    print(data)
    sock.send(data.encode(encoding='UTF-8'))