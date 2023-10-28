from django.contrib import admin
from .models import EventsApp

# Register your models here.
@admin.register(EventsApp)
class EventsManager(admin.ModelAdmin):
    list_display = ('event_name','department','event_organizer','status')

    search_fields = ('event_name','event_organizer')

    list_filter = ('status',)

