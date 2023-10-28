"""DOCUMENTATION TAG

1. We are designing the layout and appearance via the @admin.register()
2. We are creating a Single database to handle all the career Advice Given

"""
from django.contrib import admin

from .models import CareerAdvice

# STYLE THE ADMIN INTERFACE DESIGN FOR THIS APPLICATION
@admin.register(CareerAdvice)
class CareerAdmin(admin.ModelAdmin):
    #Show this default information
    list_display = ('person_name','position','company','status')

    #Use these tags for filtering of the data
    list_filter = ('status','created','company')

    #Allow for the searching of some keywords
    search_fields = ('title_of_advice','the_advise','created')

    #Allow for easier identification of the author
    raw_id_fields = ('author',)

    
