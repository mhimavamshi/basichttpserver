from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from HTTPRequest import *
from HTTPResponse import *
from threading import Thread

class StaticHTTPServer:
    def __init__(self, log=True, **kwargs):
        self.host, self.port = kwargs['host'], kwargs['port']
        self.tcp_sock = socket(AF_INET, SOCK_STREAM)
        self.tcp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.tcp_sock.bind((self.host, self.port))
        self.should_log = log

    def log(self, message):
        if self.should_log: print(message)

    def handle_client(self, client_sock, address):
        raw_data = client_sock.recv(1024)
        # self.log("Raw data: "+str(raw_data)+" from "+str(address))
        # TODO: listen to the http request header info, don't just respond
        request = HTTPRequest(raw_data)
        self.log("\n"+str(address)+": "+request.info()+"\n")

        # TODO: handle paths better, a hack for now 
        file_path = "."+request.path

        if request.method in {'POST', 'HEAD'}:
            response = HTTPResponse(status_code=400) 

        if request.method == "GET":
            if not os.path.isfile(file_path):
                response = HTTPResponse(status_code=404)
            else:
                response = HTTPResponse(status_code=200, file_path=file_path)

        client_sock.send(response.make())        
        self.log(f"Sent \n------\n{response}\n------\n to client with address {address}")

    def serve(self):
        print(f"Server will listen at {self.host}:{self.port}")
        self.tcp_sock.listen(5)
        
        while True:
            client_sock, address = self.tcp_sock.accept()
            client_thread = Thread(target=self.handle_client, args=(client_sock, address))
            client_thread.start()



