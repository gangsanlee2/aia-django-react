from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    user_email: str
    password: str
    user_name: str
    phone: str
    birth: str
    address: str
    job: str
    user_interests: str
    token: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True