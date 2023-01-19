from abc import abstractmethod, ABCMeta
from typing import List

from app.models.article import Article
from app.schemas.article import ArticleDTO, IndivArticleDTO


class ArticleBase(metaclass=ABCMeta):

    @abstractmethod
    def add_article(self, request_article: IndivArticleDTO) -> str: pass

    @abstractmethod
    def update_article(self, request_article: IndivArticleDTO) -> str: pass

    @abstractmethod
    def delete_article(self, request_article: IndivArticleDTO) -> str: pass

    @abstractmethod
    def find_all_articles_per_page(self, page: int) -> List[Article]: pass

    @abstractmethod
    def find_all_articles(self) -> List[ArticleDTO]: pass

    @abstractmethod
    def find_article_by_seq(self, request_article: ArticleDTO) -> Article: pass

    @abstractmethod
    def find_articles_by_user_id(self, request_article: ArticleDTO, page: int) -> List[Article]: pass

    @abstractmethod
    def find_articles_by_title(self, title: str, page: int) -> List[Article]: pass

    @abstractmethod
    def match_token_for_article(self, request_article: IndivArticleDTO) -> bool: pass

    @abstractmethod
    def find_all_articles_ordered(self) -> List[Article]: pass

    @abstractmethod
    def count_all_articles(self) -> int: pass


