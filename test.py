from server import StaticHTTPServer

http_server = StaticHTTPServer(host='172.30.72.50', port=5000, file="./index.html", path="/")
http_server.serve()