from django.urls import path
from . import views

app_name = 'galleryApp'

urlpatterns = [
    path('',views.showGallery, name="gallery"),
]

