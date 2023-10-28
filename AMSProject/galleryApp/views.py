from django.shortcuts import render
from .models import AlumniGallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def showGallery(request):
    gallery_list = AlumniGallery.publishedGallery.all()
    
    return render(request,'gallery/index.html',{'gallery_list':gallery_list})
