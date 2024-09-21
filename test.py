from server import StaticHTTPServer

http_server = StaticHTTPServer(host='0.0.0.0', port=5000, file="index.html", path="/")
http_server.serve()