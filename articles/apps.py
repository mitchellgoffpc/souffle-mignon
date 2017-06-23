import algoliasearch_django as algoliasearch

from django.apps import AppConfig

from articles.index import ArticleIndex


class ArticleConfig(AppConfig):
    name = 'articles'

    def ready(self):
        Article = self.get_model('Article')
        algoliasearch.register(Article, ArticleIndex)
