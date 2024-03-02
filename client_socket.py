import socket

def clientProgram():
    host = socket.gethostname()
    port = 5000

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host,port))

    message = input('->')

    while message.lower().strip() != 'bye':
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()

        print('Received from server:' + data)
        message = input('->')

    clientSocket.close()

if __name__ == '__main__':
    clientProgram()