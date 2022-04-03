import socket


class Client():
    def __init__(self) -> None:
        self.host = socket.gethostbyname(socket.gethostname()) # Get host name
        self.port  = 5050
        self.format = 'utf-8'

    def connect(self):
        '''Connect in server'''
        print('new client to server connection')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((self.host, self.port))
        server.sendall(str.encode('Test of connection'))
        data = server.recv(1024)
        print(f'status: {data.decode()}')
        server.close()

if __name__ == '__main__':
    my_client = Client()
    my_client.connect()

