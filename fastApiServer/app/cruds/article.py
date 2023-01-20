from abc import ABC
from app.bases.article import ArticleBase
from app.models.article import Article
from app.schemas.article import ArticleDTO, IndivArticleDTO
from app.models.user import User
from sqlalchemy.orm import Session
from typing import List
import pymysql
pymysql.install_as_MySQLdb()


class ArticleCrud(ArticleBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_article(self, request_article: IndivArticleDTO) -> str:
        indiv_article = request_article.dict()
        user = self.db.query(User).filter(User.token == indiv_article['token']).one_or_none()
        is_success = self.db.add(Article(title=indiv_article['title'], content=indiv_article['content'], user_id=user.user_id))
        self.db.commit()
        return "article is successfully written" if is_success != 0 else "it's failed to write article"

    def update_article(self, request_article: IndivArticleDTO) -> str:
        indiv_article = request_article.dict()
        user = self.db.query(User).filter(User.token == indiv_article['token']).one_or_none()
        is_success = self.db.query(Article).filter(Article.user_id == user.user_id).\
            filter(Article.art_seq == indiv_article["art_seq"]).\
            update({"title": indiv_article["title"], "content": indiv_article["content"]})
        self.db.commit()
        return "article is successfully updated" if is_success != 0 else "it's failed to update article"

    def delete_article(self, request_article: IndivArticleDTO) -> str:
        indiv_article = request_article.dict()
        user = self.db.query(User).filter(User.token == indiv_article['token']).one_or_none()
        target = self.db.query(Article).filter(Article.user_id == user.user_id).\
            filter(Article.art_seq == indiv_article["art_seq"]).one_or_none()
        is_success = self.db.delete(target)
        self.db.commit()
        return "article is successfully deleted" if is_success != 0 else "it's failed to delete article"

    def find_all_articles(self) -> List[ArticleDTO]:
        return self.db.query(Article).all()

    def find_article_by_seq(self, seq: int) -> ArticleDTO:
        return self.db.query(Article).filter(Article.art_seq == id).one_or_none()

    def find_articles_by_user_id(self, request_article: ArticleDTO, page: int) -> List[ArticleDTO]:
        print(f"### page number is {page}")
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.user_id == article.user_id).all()

    def find_articles_by_title(self, title: str, page: int) -> List[ArticleDTO]:
        print(f"### page number is {page}")
        return self.db.query(Article).filter(Article.title == title).all()

    def match_token_for_article(self, request_article: IndivArticleDTO) -> bool:
        article_token = request_article.dict()["token"]
        user = self.db.query(User).filter(User.token == article_token).one_or_none()
        db_user = self.db.query(User).filter(User.user_id == user.user_id).one_or_none()
        return True if db_user is not None else False

    def find_all_articles_ordered(self) -> List[Article]:
        return self.db.query(Article).order_by(Article.art_seq).all()
