from datetime import datetime, timezone

def get_http_date():
    current_time = datetime.now(timezone.utc)
    return current_time.strftime('%a, %d %b %Y %H:%M:%S GMT')

def timestamp_to_httpdate(timestamp):
    date = datetime.fromtimestamp(timestamp, timezone.utc)
    return date.strftime('%a, %d %b %Y %H:%M:%S GMT')

if __name__ == "__main__":
    print("Current HTTP date:", get_http_date())
    example_timestamp = 1633072800 
    print("Converted HTTP date:", timestamp_to_httpdate(example_timestamp))