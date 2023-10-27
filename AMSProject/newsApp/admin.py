from django.contrib import admin
from .models import Article, Comment

#admin.site.register(Article)

#To style the appearance of the django admin interface
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #Determine the appearance on the landing page
    list_display = ('title','slug','author','publish','status')
    
    #Add the ability to filter the results
    list_filter = ('status','created','publish','author',)

    #Add the ability to search inside the articles for keywords
    search_fields = ('title','body')

    #Add the auto populated fields, especially the url slug
    prepopulated_fields = {'slug':('title',)}

    #Add the fields of the names to be changed
    raw_id_fields = ('author',)

    #Update the date hierarchyy
    date_hierarchy = 'publish'

    #Replace the ordering and use this feature
    ordering = ('status','-publish')

#Register the Comments
#admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','article','created')


