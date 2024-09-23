import os

class HTTPResponse:
    status_readable = {
        404: "Not Found",
        400: "Bad Request",
        200: "OK",
        301: "Moved Permanently"
    }

    # TODO: don't just trust the extensions, check the file's head and content and everything else and infer
    # placeholder for now
    extension_to_mime = {
        'html': 'text/html',
        'htm': 'text/html',
        'css': 'text/css',
        'py': 'text/plain',
        'js': 'text/javascript',
        'json': 'application/json',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'svg': 'image/svg+xml',
        'txt': 'text/plain',
        'pdf': 'application/pdf',
        'zip': 'application/zip',
    }

    def __init__(self, status_code=200, headers={}, body=None, redirection_location="/index.html"):
        self.status_code = status_code
        self.redirection_location = redirection_location
        self.headers = {}
        self.start_line = self.make_response_line()
        self.body = self.make_body(body) 
        self.headers = self.make_headers(headers)
        self.raw_message = self.make()


    def make_headers(self, headers):
        self.headers.update(headers)
        return "\r\n".join(": ".join(item) for item in self.headers.items())

    def make_response_line(self):
        return f"HTTP/1.0 {self.status_code} {HTTPResponse.status_readable[self.status_code]}"

    # TODO: don't read from disk for every response making, use a "cache"
    def make_body(self, body=None):
        if self.status_code == 400:
            self.headers['Content-Type'] = "text/plain"
            self.headers['Content-Length'] = "18"
            return "\r\nUnsupported Method"
        # Hmmm, Should it be hardcoded? or a seperate file or something else? 
        if self.status_code == 404:
            self.headers['Content-Type'] = "text/plain"
            self.headers['Content-Length'] = "16"
            return "\r\n404 Not Found :("
        
        if self.status_code == 301:
            self.headers['Location'] = self.redirection_location
            self.headers['Content-Length'] = "0"
            return "\r\n"

        # if self.status_code == 200 and file_path == None:
        #     raise Exception("No file was provided to serve the GET request.")

        # try:
        #     self.headers["Content-Type"] = HTTPResponse.extension_to_mime[file_path.rsplit('.', 1)[-1]]
        # except KeyError:
        #     # TODO: is 200 a good idea?
        #     print(file_path.rsplit('.', 1)[-1])
        #     self.headers["Content-Length"] = "0"
        #     return "\r\n"

        self.headers["Content-Type"] = body[0]
        self.headers["Content-Length"] = body[1]
        # self.headers["Expires"] = 
        # self.headers["Last-Modified"] =
        return "\r\n" + str(body[2])


    def make(self):
        self.message = "\r\n".join((self.start_line, self.headers, self.body))
        return bytes(self.message, encoding="utf-8")
    
    def __str__(self):
        return f"{self.start_line}\n{self.headers}\n{self.body[0:20]}...."
