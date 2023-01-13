from sqlalchemy import Column, TIMESTAMP as Timestamp, text


class TimeStampMixin(object):
    created_at = Column(Timestamp(timezone=True), nullable=False, server_default=text('current_timestamp'))
    updated_at = Column(Timestamp(timezone=True), nullable=False, server_default=text('current_timestamp on update current_timestamp'))