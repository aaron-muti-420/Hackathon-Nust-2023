from django.shortcuts import render
#Import the Database
from .models import CareerAdvice

from django.shortcuts import render, get_object_or_404
#Allow Adding a tag to our views
from taggit.models import Tag

# CLASS BASED VIEWS IMPORTS
from django.views.generic import ListView

#When the articles have become increasingly numerous, adding pagination becomes a great idea
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# class CareerAdviceListView(ListView):
#     queryset = CareerAdvice.publishedAdvice.all()
#     context_object_name = 'career_advice'
#     paginate_by = 12
#     template_name = 'career/list_advice.html'

# WE ARE USING THE FUNCTIONAL PROGRAMMING METHOD IN THIS REGARD

def CareerAdviceListView(request, tag_slug=None):
    #Retrieve all published articles alone
    advice_list = CareerAdvice.publishedAdvice.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)

        advice_list = advice_list.filter(tags__in=[tag])

    # Initialize the paginator with default number of posts
    paginator = Paginator(advice_list, 8)

    #The GET parameter indicates the current page number
    page = request.GET.get('page')

    try:
        advice = paginator.page(page)
    except PageNotAnInteger:
        #Should the page not be an int then it has to be the 1st one
        advice = paginator.page(1)
    except EmptyPage:
        #If the page is out of the range then deliver the last page of results
        advice = paginator.page(paginator.num_pages)

    #Use the imported render shortcut to show all posts
    return render(request, 'career/list_advice.html',  {
            'page':page,
            'advice':advice,
            'tag':tag
        })




