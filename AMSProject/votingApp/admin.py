from django.contrib import admin
from .models import Question, Choice

#Create 4 extra lines in order to allow for more options
# With the option of removing or readding
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


#admin.site.register(Question, QuestionAdmin)
@admin.register(Question)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ('question_text','pub_date')


