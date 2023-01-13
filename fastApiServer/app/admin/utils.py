from datetime import datetime
from pytz import timezone


def currentTime():
    today = datetime.now(timezone('Asia/Seoul'))
    return f'{today.time().strftime("%H:%M:%S")}'
