from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

from app.cruds.article import ArticleCrud
from app.database import get_db
from app.schemas.article import ArticleDTO, IndivArticleDTO

router = APIRouter()

@router.post("/write")
async def new_article(dto: IndivArticleDTO, db: Session = Depends(get_db)):
    if ArticleCrud(db).match_token_for_article(request_article=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=ArticleCrud(db).add_article(request_article=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/update")
async def update(dto: IndivArticleDTO, db: Session = Depends(get_db)):
    if ArticleCrud(db).match_token_for_article(request_article=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=ArticleCrud(db).update_article(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.delete("/delete")
async def delete(dto: IndivArticleDTO, db: Session = Depends(get_db)):
    if ArticleCrud(db).match_token_for_article(request_article=dto):
        article_crud = ArticleCrud(db)
        message = article_crud.delete_article(dto)
        return JSONResponse(status_code=400, content=dict(msg=message))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.get("/page/{page}")
async def get_articles(page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_all_articles_per_page(page)
    return result

@router.get("/list")
async def get_all_articles(db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    ls = article_crud.find_all_articles()
    return {"data": ls}

@router.get("/seq/{id}")
async def get_article_by_seq(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_article_by_seq(dto)
    return result

@router.get("/user/{id}/page/{page}")
async def get_articles_by_user(dto: ArticleDTO, page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_articles_by_user_id(dto, page)
    return result

@router.get("/title/{search}/page/{page}")
async def get_articles_by_title(title: str, page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_articles_by_title(title, page)
    return result