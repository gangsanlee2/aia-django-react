from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .mixins import TimeStampMixin
from ..database import Base


class User(Base, TimeStampMixin):

    __tablename__ = "users"

    user_id = Column(String(30), primary_key=True)
    user_email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(100))
    job = Column(String(20))
    user_interests = Column(String(100))
    token = Column(String(256))

    articles = relationship('Article', back_populates='user')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'아이디: {self.user_id}, \n ' \
               f'이름: {self.user_name}, \n ' \
               f'이메일: {self.user_email} \n ' \
               f'비번: {self.password} \n' \
               f'전화번호: {self.phone} \n' \
               f'생년월일: {self.birth} \n' \
               f'주소: {self.address} \n' \
               f'직업: {self.job} \n' \
               f'관심사: {self.user_interests} \n' \
               f'토큰: {self.token} \n' \
               f'작성일: {self.created_at} \n' \
               f'수정일: {self.updated_at}'