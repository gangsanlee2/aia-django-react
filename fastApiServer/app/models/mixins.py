from datetime import datetime, timedelta

from sqlalchemy import Column, TIMESTAMP as Timestamp, text


class TimeStampMixin(object):
    # 23.01.16. 기준 둘다 현재 서울 시각으로 반영 됐음
    '''
    created_at = Column(Timestamp(timezone=True), nullable=False, server_default=text('current_timestamp'))
    updated_at = Column(Timestamp(timezone=True), nullable=False, server_default=text('current_timestamp on update current_timestamp'))
    '''
    kst = datetime.utcnow() + timedelta(hours=9)  # 한국 표준시인 KST는 UTC로부터 9시간을 더하면 된다
    now = kst.strftime("%Y-%m-%d %H:%M:%S")
    created_at = Column(Timestamp, nullable=False, default=now)
    updated_at = Column(Timestamp, nullable=False, default=now)

