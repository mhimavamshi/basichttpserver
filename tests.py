from server import HTTPResponse

r = HTTPResponse()
print(r.make_headers(content_type="text/html", Cache="public"))