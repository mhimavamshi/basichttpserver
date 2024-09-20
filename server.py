import os
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


# TODO: make the parsing prettier and improve on it

class HTTPRequest:
    def __init__(self, raw_data):
        self.data = raw_data.decode("utf-8")
        self.lines = self.data.split("\r\n")
        self.start_line = self.lines[0].split(" ")
        self.method, self.path, self.http_version = self.start_line

        self.headers = [header.replace(" ", "").split(":") for header in self.lines[1:]]

    def is_get_for(self, path):
        return self.path == path and self.method == "GET"
    
    def string(self):
        return f"{self.method} request to path {self.path}"

    def __str__(self):
        return f"{self.start_line}, {self.headers}"

# TODO: make the response more general; for now it's just 200 status and no headers
class HTTPResponse:
    def __init__(self, html_body, length):
        self.start_line = "HTTP/1.1 200 OK"
        self.content_length = str(length)
        # Hardcoded, not good
        self.message = self.start_line + "\r\n" + "Content-Length: " + self.content_length + "\r\n" + "Content-Type: text/html\r\n\r\n" + html_body + "\r\n"
    
    def make(self):
        return bytes(self.message, encoding="utf-8")

# TODO: make it more general; capable of serving static html files at various paths/routes
class StaticHTTPServer:
    def __init__(self, log=True, **kwargs):
        self.host, self.port = kwargs['host'], kwargs['port']
        self.html_file_path = kwargs['file']
        self.path = kwargs['path']
        self.tcp_sock = socket(AF_INET, SOCK_STREAM)
        self.tcp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.tcp_sock.bind((self.host, self.port))
        self.should_log = log

    def log(self, message):
        if self.should_log: print(message)

    def serve(self):
        with open(self.html_file_path, 'r') as fl:
            html_body = fl.read()

        length = os.path.getsize(self.html_file_path)
        http_response = HTTPResponse(html_body, length)

        print(f"Server will listen at {self.host}:{self.port}")
        self.tcp_sock.listen(5)
        
        while True:
            client_sock, address = self.tcp_sock.accept()
            request = HTTPRequest(client_sock.recv(1024))
            self.log(str(address)+": "+request.string())
            if request.is_get_for(self.path):
                self.log(f"Served the {self.html_file_path} to client with address {address}")
                client_sock.send(http_response.make())
