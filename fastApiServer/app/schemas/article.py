from typing import Optional

from pydantic import BaseModel


class ArticleDTO(BaseModel):
    art_seq: Optional[int]
    title: Optional[str]
    content: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    user_id: Optional[str]

    class Config:
        orm_mode = True

class IndivArticleDTO(BaseModel):
    title: Optional[str]
    content: Optional[str]
    token: Optional[str]

    class Config:
        orm_mode = True