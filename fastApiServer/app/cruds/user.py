from abc import ABC
from typing import List

from fastapi import HTTPException
from sqlalchemy import select

from app.admin.security import verify_password, generate_token, get_hashed_password, myuuid
from app.bases.user import UserBase
from app.database import conn
from app.models.user import User
import pymysql
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()
from app.schemas.user import UserDTO, UserUpdate

from fastapi_pagination import Page, paginate, add_pagination


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        user_id = self.find_user_by_email(request_user=request_user)
        if user_id == "":
            user.user_id = myuuid()
            user.password = get_hashed_password(user.password)
            is_success = self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            message = "SUCCESS: 회원가입이 완료되었습니다" if is_success != 0 else "FAILURE: 회원가입이 실패하였습니다"
        else:
            message = "FAILURE: 이메일이 이미 존재합니다"
        return message

    def login(self, request_user: UserDTO) -> str:
        user_id = self.find_user_by_email(request_user=request_user)
        if user_id != "":
            request_user.user_id = user_id
            db_user = self.find_user_by_id(request_user)
            verified = verify_password(plain_password=request_user.password,
                                       hashed_password=db_user.password)
            if verified:
                new_token = generate_token(request_user.user_email)
                request_user.token = new_token
                self.update_token(db_user, new_token)
                return new_token
            else:
                return "FAILURE: 비밀번호가 일치하지 않습니다"
        else:
            return "FAILURE: 이메일 주소가 존재하지 않습니다"

    def logout(self, request_user: UserDTO) -> str:
        user = self.find_user_by_token(request_user)
        is_success = self.db.query(User).filter(User.user_id == user.user_id).update({User.token: ""})
        self.db.commit()
        print(f"토큰 삭제되면 1 : {is_success}")
        return "로그아웃 성공입니다." if is_success != 0 else "로그아웃 실패입니다."

    def update_user(self, request_user: UserUpdate) -> str:
        db_user = self.find_user_by_id_for_update(request_user)
        for var, value in vars(request_user).items():
            setattr(db_user, var, value) if value else None
        is_success = self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return "success" if is_success != 0 else "failed"

    def update_token(self, db_user: User, new_token: str) -> str:
        is_success = self.db.query(User).filter(User.user_id == db_user.user_id) \
            .update({User.token: new_token}, synchronize_session=False)
        self.db.commit()
        self.db.refresh(db_user)
        return "success" if is_success != 0 else "failed"

    def update_password(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        user.password = get_hashed_password(user.password)
        is_success = self.db.query(User).filter(User.user_id == user.user_id) \
            .update({User.password: user.password}, synchronize_session=False)
        self.db.commit()
        return "success" if is_success != 0 else "failed"

    def delete_user(self, request_user: UserDTO) -> str:
        user = self.find_user_by_id(request_user)
        print(f"### user is : ### \n{user}")
        is_success = self.db.query(User).filter(User.user_id == user.user_id).delete(synchronize_session=False)
        self.db.commit()
        return "탈퇴 성공입니다." if is_success != 0 else "탈퇴 실패입니다."

    def find_all_users_ordered(self) -> List[User]:
        return self.db.query(User).order_by(User.created_at).all()

    def find_user_by_token(self, request_user: UserDTO) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.token == user.token).one_or_none()

    def find_user_by_id(self, request_user: UserDTO) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.user_id == user.user_id).one_or_none()

    def find_user_by_id_for_update(self, request_user: UserUpdate) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.user_id == user.user_id).one_or_none()

    def find_user_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.user_email == user.user_email).one_or_none()
        if db_user is not None:
            return db_user.user_id
        else:
            return ""

    def find_all_users(self) -> List[User]:
        return self.db.query(User).all()

    def match_token(self, request_user: UserDTO) -> bool:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.token == user.token).one_or_none()
        return True if db_user != None else False

    def match_token_for_modify(self, request_user: UserUpdate) -> bool:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.token == user.token).one_or_none()
        return True if db_user != None else False

    def count_all_users(self) -> int:
        return self.db.query(User).count()



'''
def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()
'''
