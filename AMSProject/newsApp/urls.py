from django.urls import path
from . import views

app_name = 'newsApp'

# urlpatterns = [
#     #Article Views
#     path('',views.article_list, name='article_list'),
#     # Year, month and day require integer values while a slug allows words and hyphens
#     #Angle prackets are used to capture values from the url, all values between them are seen as string
#     path('<int:year>/<int:month>/<int:day>/<slug:article>/', views.article_details,name="article_details"),
# ]

# Visit https://docs.djangoproject.com/en/3.0/topics/http/urls/#path-converters
# Visit https://docs.djangoproject.com/en/3.0/ref/urls/#django.urls.re_path

""" 
CLASS BASED VIEWS URLSPATTERNS
"""

urlpatterns = [
    path('', views.article_list,name='article_list'),

    path('tag/<slug:tag_slug>/',views.article_list, name="article_list_by_tag"),
    
    path('<int:year>/<int:month>/<int:day>/<slug:article>/', views.article_details,name="article_details"),

    path('<int:article_id>/share/',views.share_article, name='article_share'),
]


