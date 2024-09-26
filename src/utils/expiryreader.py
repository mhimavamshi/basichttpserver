import mimetypes
import os
from src.utils.httpdate import timestamp_to_httpdate

class ExpiryReader:
    def __init__(self, infopath):
        self.filetypes = mimetypes.types_map.keys()
        with open(infopath, "r") as fl:
            self.raw_data = fl.read()
        self.expires = {}
        self.time_vals = {
            'm': 2592000,
            'y': 31536000,
            'd': 86400,
        }
        self.parse()

    def parse(self):
        lines = self.raw_data.split("\n")
        for line in lines:
            refer, time = line.split(" ")
            # print(f"\nParsing time for {refer}")
            self.expires[refer] = self.parse_time(time)
            
    # TODO: maybe use regex
    def parse_time(self, time):
        stack = []
        digit_place = 0
        total = 0
        for ch in time:
            if ch.isdigit(): 
                stack.append(int(ch))
                continue
            
            while len(stack) != 0:
                total += stack.pop() * (10 ** digit_place)
                digit_place += 1
            
            # print(f"TOTAL: {total}")
            total *= self.time_vals[ch]
            # print(f"TOTAL: {total} with {ch}")

            digit_place = 0
            
        return total


    def of(self, file_path):
        # mtime = os.path.getmtime(file_path)
        # ctime = os.path.getctime(file_path)
        atime = os.path.getatime(file_path)
        mimetype, _ = mimetypes.guess_type(file_path) # maybe redundant? probably called before; check
        expiry = self.expires[mimetype]
        return timestamp_to_httpdate(atime + expiry)

if __name__ == "__main__":
    path = "../../expires.info"
    reader = ExpiryReader(path)
    print(reader.expires)
    dpath = "../../testdirectory/"
    files = list(map(lambda file: dpath + file, os.listdir(dpath)))
    for file in files:
        print(f"For {file} - Expires: {reader.of(file)}")