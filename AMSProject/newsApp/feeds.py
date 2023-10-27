"""DOCUMENTATION ANNOTATION

1. This page is for generating dynamic RSS or Atom Feeds to create sitemaps
2. Users will be able to subscribe to the feed using a feed aggregator
3. This software will be able to get new content notifications

"""

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Article

class LatestPostsFeed(Feed):

    """
        The title correspond with <title>,
        link, and correspond with <link>,
        description correspond with <description> 

        Of the RSS Feed

    """
    title = 'Nust | AMS'
    #Generate a link with the reverse lazy before configuring the urls.py
    link = reverse_lazy('newsApp:article_list')
    description = 'New articles of the Nust Alumni Management System'

    def items(self):
        return Article.publishedArticles.all()[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatewords(item.body, 30)





