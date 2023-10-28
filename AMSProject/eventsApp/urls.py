from django.urls import path
from . import views

app_name = 'eventsApp'

urlpatterns = [
    path('',views.upcomingEvents, name="upcoming_events"),
]
