from django.contrib import admin
from .models import AlumniGallery

# Register your models here.
@admin.register(AlumniGallery)
class GalleryManager(admin.ModelAdmin):
    
    list_display = ('name_of_event','event_location',)


