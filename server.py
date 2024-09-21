from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from HTTPRequest import *
from HTTPResponse import *


class StaticHTTPServer:
    def __init__(self, log=True, **kwargs):
        self.host, self.port = kwargs['host'], kwargs['port']
        self.path = kwargs['path']
        self.tcp_sock = socket(AF_INET, SOCK_STREAM)
        self.tcp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.tcp_sock.bind((self.host, self.port))
        self.should_log = log

    def log(self, message):
        if self.should_log: print(message)

    def serve(self):
        print(f"Server will listen at {self.host}:{self.port}")
        self.tcp_sock.listen(5)
        
        while True:
            client_sock, address = self.tcp_sock.accept()
            raw_data = client_sock.recv(2048)
            # self.log("Raw data: "+str(raw_data)+" from "+str(address))
            # TODO: listen to the http request info, don't just respond
            request = HTTPRequest(raw_data)
            self.log(str(address)+": "+request.string())

            # TODO: handle paths better, a hack for now 
            file_path = "."+request.path

            if request.method in {'POST', 'HEAD'}:
                response = HTTPResponse(status_code=400) 

            if not os.path.exists(file_path):
                response = HTTPResponse(status_code=404)
            elif request.method == "GET":
                response = HTTPResponse(status_code=200, file_path=file_path)
            
            self.log(f"Sent \n{response}\n to client with address {address}")
            client_sock.send(response.make())


