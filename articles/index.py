from algoliasearch_django import AlgoliaIndex

class ArticleIndex(AlgoliaIndex):
    settings = {'searchableAttributes': ['title', 'slug', 'author', 'entry']}
