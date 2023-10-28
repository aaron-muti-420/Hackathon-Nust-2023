from django.urls import path
from . import views

app_name = 'careeerAdviceApp'

urlpatterns = [
    #The commented out view is only used with the Class based views
    #path('',views.CareerAdviceListView.as_view(),name='list_career'),
    
    #Allow the page to show the list of the items that need to be immediately displayed without the tag added on
    path('', views.CareerAdviceListView,name='advice_list'),

    #Allow the viewing of the advice based on the attached tag
    path('tag/<slug:tag_slug>/',views.CareerAdviceListView, name="advice_list_by_tag"),
    
]


