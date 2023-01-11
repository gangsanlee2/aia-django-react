from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.repositories.article as dao     # DAO data access object
from app.database import get_db
from app.schemas.article import Article

router = APIRouter()

@router.post("/")
async def write(id: str, item: Article, db: Session = Depends(get_db)):
    post_dict = item.dict()
    print(f"New Article Inform : {post_dict}")
    dao.new_article(id, item, db)
    return {"data": "success"}

@router.put("/{id}")
async def update(id: str, item: Article, db: Session = Depends(get_db)):
    dao.update(id,item,db)
    return {"data": "success"}

@router.delete("/{id}")
async def delete(id: str, item: Article, db: Session = Depends(get_db)):
    dao.delete(id,item,db)
    return {"data": "success"}

@router.get("/{page}")
async def get_articles(page: int, db: Session = Depends(get_db)):
    ls = dao.find_articles(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_article(id: str, db: Session = Depends(get_db)):
    dao.find_article(id, db)
    return {"data": "success"}

@router.get("/title/{search}/{page}")
async def get_articles_by_title(search: str, page: int, db: Session = Depends(get_db)):
    dao.find_articles_by_title(search, page, db)
    return {"data": "success"}