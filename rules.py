from datetime import datetime

def parse_time(line):
    return datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")