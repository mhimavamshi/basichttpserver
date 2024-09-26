from src.server import StaticHTTPServer
from src.utils.expiryreader import ExpiryReader

reader = ExpiryReader("./expires.info")

http_server = StaticHTTPServer(host='0.0.0.0', port=5000, expiryreader=reader)
# no freedom here.... serves the current directory
http_server.serve()