from pydantic import BaseConfig
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from .mixins import TimeStampMixin
from ..admin.security import myuuid
from ..database import Base


class Article(Base, TimeStampMixin):

    __tablename__ = "articles"

    art_seq = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(20), nullable=False)
    content = Column(String(20), nullable=False)

    #user_id = Column(UUIDType(binary=False), ForeignKey("users.user_id"), nullable=True)
    user_id = Column(String(30), ForeignKey("users.user_id"), default=myuuid())

    user = relationship('User', back_populates='articles')

    class Config:
        BaseConfig.arbitrary_types_allowed = True

    def __str__(self):
        return f'글번호: {self.art_seq}, \n ' \
               f'제목: {self.title}, \n ' \
               f'내용: {self.content} \n ' \
               f'글쓴이: {self.user_id} \n' \
               f'작성일: {self.created_at} \n' \
               f'수정일: {self.updated_at}'