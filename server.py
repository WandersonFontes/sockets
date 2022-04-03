import socket


class Server():
    def __init__(self) -> None:
        self.host = socket.gethostbyname(socket.gethostname()) # Get host name
        self.conections_number = 0
        self.port  = 5050
        self.format = 'utf-8'

    def start(self):
        '''Start server for new connections'''
        # socket(Protocol family, Protocol Type)
        # socket(IPV4, UDP)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'host: {self.host}\nport: {self.port}')
        server.bind((self.host, self.port))
        print('started sucessfully')

        server.listen()

        while True:
            print(f'waiting for new connections...')

            connect, address = server.accept() # Accept new conections
            print(f'{"-"*50}\nconnected in {address}')
            self.conections_number = self.conections_number + 1

            data = connect.recv(1024).decode(self.format)
            print(f'msg: {data}')
            print(f'total conections: {self.conections_number}\n{"-"*50}')
            connect.sendall(str.encode(f'Conected sucessfully, index {self.conections_number}!'))

            if int(self.conections_number) == 15:
                print('maximum connections reached\nclosed server!')
                server.close()
                break
            
if __name__ == '__main__':
    my_server = Server()
    my_server.start()
        
        
