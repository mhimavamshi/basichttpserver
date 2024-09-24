from socket import SHUT_RDWR, socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from HTTPRequest import *
from HTTPResponse import *
from threading import Thread
import mimetypes

class StaticHTTPServer:
    def __init__(self, log=True, **kwargs):
        self.host, self.port = kwargs['host'], kwargs['port']
        self.client_threads = []
        self.tcp_sock = socket(AF_INET, SOCK_STREAM)
        self.tcp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.tcp_sock.bind((self.host, self.port))
        self.should_log = log
        self.file_cache = {}

    def log(self, message, mtype="INFO"):
        if self.should_log: 
            print(f"[{mtype}]:" , message)

    def handle_client(self, client_sock, address):
        raw_data = client_sock.recv(1024)
        # self.log("Raw data: "+str(raw_data)+" from "+str(address))
        # TODO: listen to the http request header info, don't just respond
        request = HTTPRequest(raw_data)
        self.log("\n"+str(address)+": "+request.info()+"\n")

        if request.method in {'POST', 'HEAD'}:
            response = HTTPResponse(status_code=400) 

        # TODO: handle paths better, a hack for now 
        file_path = os.path.normpath("." + request.path)

        if request.method == "GET":
            if request.path == "/":
                response = HTTPResponse(status_code=301, redirection_location="/index.html")
            elif not os.path.isfile(file_path):
                response = HTTPResponse(status_code=404)
            else:

                # TODO: handle this when the files on disk change
                if file_path in self.file_cache:
                    body = self.file_cache[file_path]
                    self.log(f"Got {file_path} from file cache")
                else:
                    body = []
                    # extension = file_path.rsplit('.', 1)[-1]
                    # if extension in HTTPResponse.extension_to_mime: body.append(HTTPResponse.extension_to_mime[extension])
                    # else: body.append("text/plain")
                    mimetype, _ = mimetypes.guess_type(file_path)
                    if mimetype == None: body.append("text/plain")
                    else: body.append(mimetype)
                    body.append(str(os.path.getsize(file_path)))
                    with open(file_path, "rb") as fl: body.append(fl.read())
                    self.file_cache[file_path] = body             
                    self.log(f"Added {file_path} to file cache")

                response = HTTPResponse(status_code=200, body=body)

        client_sock.send(response.make())        
        self.log(f"Sent \n------\n{response}\n------\n to client with address {address}")


        try:
            client_sock.shutdown(SHUT_RDWR)
            client_sock.close()
        except Exception as exp:
            self.log(f"{exp} encountered while shutting down client socket", mtype="ERROR")

    def serve_loop(self):
        print(f"Server will listen at {self.host}:{self.port}")
        self.tcp_sock.listen(5)
        
        while True:
            client_sock, address = self.tcp_sock.accept()
            client_thread = Thread(target=self.handle_client, args=(client_sock, address))
            self.client_threads.append(client_thread)
            client_thread.start()

    def serve(self):
        try:
            self.serve_loop()
        except KeyboardInterrupt:
            self.log("\nServer shutting down....")
        finally:
            for client_thread in self.client_threads:
                if client_thread.is_alive(): client_thread.join()
            self.tcp_sock.close()
            self.log("Server has shut down")


