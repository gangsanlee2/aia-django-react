from datetime import datetime
from pytz import timezone


def currentTime():
    today = datetime.now(timezone('Asia/Seoul'))
    return f'{today.time().strftime("%H:%M:%S")}'

def utc_seoul():
    return datetime.now(timezone('Asia/Seoul'))

if __name__ == '__main__':
    print(currentTime())