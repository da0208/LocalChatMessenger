import socket
from faker import Faker

def serverProgram():
    host = socket.gethostname()
    port = 5000

    serverSocket = socket.socket()
    serverSocket.bind((host,port))

    print('Server is listening...')
    serverSocket.listen(2)
    conn,address = serverSocket.accept()
    print('Connection from:' + str(address))

    faker = Faker()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('from connected user:' + str(data))

        data = faker.sentence()
        conn.send(data.encode())
    
    conn.close()

if __name__ == '__main__':
    serverProgram()