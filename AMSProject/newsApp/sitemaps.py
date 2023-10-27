#Enabling web crawlers to better index our site
from django.contrib.sitemaps import Sitemap

from .models import Article

class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    #Maximum priority value is 1
    priority = 0.9

    def items(self):
        return Article.publishedArticles.all()
    
    def lastmod(self, obj):
        return obj.updated



