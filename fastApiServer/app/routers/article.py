from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

from app.cruds.article import ArticleCrud
from app.database import get_db
from app.schemas.article import ArticleDTO, IndivArticleDTO
from fastapi_pagination import paginate, Page, Params
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
        return JSONResponse(status_code=400,
                            content=dict(
                                msg=ArticleCrud(db).delete_article(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.get("/page/{page}")
async def get_articles_per_page(page: int, db: Session = Depends(get_db)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = ArticleCrud(db).find_all_articles_ordered()
    page_result = paginate(results, params).dict()
    print(f"################ page_result is  \n{page_result}")
    print(f"################ 총 게시글 개수 : {page_result['total']} 개")
    return JSONResponse(status_code=200, content=jsonable_encoder(page_result))


@router.get("/page/{page}/size/{size}")
async def get_articles_per_page(page: int, size: int, db: Session = Depends(get_db)):
    params = Params(page=page, size=size)
    results = ArticleCrud(db).find_all_articles_ordered()
    page_result = paginate(results, params).dict()
    return JSONResponse(status_code=200, content=jsonable_encoder(page_result))

@router.get("/list")
async def get_all_articles(db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    ls = article_crud.find_all_articles()
    return {"data": ls}

##### 여기부터 고민할 부분 : 프런트에서 넘어오는 요청이 value(scalar)인지 아니면 dto(dictionary)인지 판단 필요 #####

@router.get("/id/{id}")
async def get_article_by_seq(seq: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_article_by_seq(seq)
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
