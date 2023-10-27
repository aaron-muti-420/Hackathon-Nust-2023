from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'newsApp'


urlpatterns = [
    path('', views.article_list,name='article_list'),

    path('tag/<slug:tag_slug>/',views.article_list, name="article_list_by_tag"),
    
    path('<int:year>/<int:month>/<int:day>/<slug:article>/', views.article_details,name="article_details"),

    path('<int:article_id>/share/',views.share_article, name='article_share'),

    #The feed system
    path('feed/', LatestPostsFeed(), name='post_feed'),

]


