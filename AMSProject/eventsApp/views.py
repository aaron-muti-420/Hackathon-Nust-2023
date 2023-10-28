from django.shortcuts import render
from .models import EventsApp

# Create your views here.

def upcomingEvents(request):
    events_list = EventsApp.publishedEvents.all()
    
    return render(request,'events/index.html',{'events_list':events_list})
