class HTTPRequest:
    def __init__(self, raw_data):
        self.data = raw_data.decode("utf-8")
        self.lines = self.data.strip().split("\r\n")
        self.method, self.path, self.protocol_version = self.parse_request_line()
        self.headers = self.parse_headers()

    def parse_request_line(self):
        return self.lines[0].split(" ")
    
    def parse_headers(self):
        headers = {}
        for line in self.lines[1:]:
            header = line.split(": ", 1)
            headers[header[0]] = header[1]
        return headers

    def string(self):
        return f"{self.method} request to path {self.path}"

    def __str__(self):
        return f"{self.method} {self.path} {self.protocol_version}\n{self.headers}"
