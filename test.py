from server import StaticHTTPServer

http_server = StaticHTTPServer(host='0.0.0.0', port=5000)
# no freedom here.... serves the current directory
http_server.serve()