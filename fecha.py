from datetime import datetime

def unix_to_timestamp(unix_time):
    dt = datetime.fromtimestamp(unix_time)
    timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
    return timestamp