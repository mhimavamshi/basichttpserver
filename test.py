from server import StaticHTTPServer

http_server = StaticHTTPServer(host='127.0.0.1', port=5000, path="./index.html", route="/")
http_server.serve()