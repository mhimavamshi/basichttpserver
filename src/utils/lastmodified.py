from src.utils.httpdate import timestamp_to_httpdate
from os.path import getmtime

class LastModifiedReader:
    @staticmethod
    def of(file):
        return timestamp_to_httpdate(getmtime(file))