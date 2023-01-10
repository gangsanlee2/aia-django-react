from pydantic import BaseModel

class Article(BaseModel):
    art_seq: int
    title: str
    content: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True