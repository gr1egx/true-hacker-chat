import socket

port = 1337

with open('banner.txt') as file:
    print(file.read())
print('WELCOME TO THE 7ru3 h4ck3r ch47')

sock = socket.socket()
sock.bind(('', port))

sock.listen()
conn, addr = sock.accept()

nick = input('Enter your nickname: ')
friend = conn.recv(1024).decode(encoding='UTF-8')
conn.send(nick.encode(encoding='UTF-8'))
print('Connection is established, u can start chatting')

while True:
    msg = str(input('Inp msg: '))
    data = ': '.join([nick, msg])
    print(data)
    conn.send(data.encode(encoding='UTF-8'))

    req_msg = conn.recv(1024)
    print(req_msg.decode(encoding='UTF-8'))