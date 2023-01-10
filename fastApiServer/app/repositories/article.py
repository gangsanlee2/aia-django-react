import pymysql
from app.database import conn
from app.models.article import Article
pymysql.install_as_MySQLdb()
from sqlalchemy.orm import Session

def find_posts_legacy():
    cursor = conn.cursor()
    sql = "select * from articles"
    cursor.execute(sql)
    return cursor.fetchall()

def find_articles(page: int, db: Session):
    print(f" page number is {page}")
    return db.query(Article).all()


def new_article(id, item, db):
    return None


def update(id, item, db):
    return None


def delete(id, item, db):
    return None


def find_article(id, db):
    return None


def find_articles_by_title(search, page, db):
    return None