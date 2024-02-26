from django.contrib import admin
from .models import Article
from django.utils import timezone

""" просто изменения"""

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'author',)
    list_display_links = ('id', 'title', 'date','author')
    search_fields = ('title', 'article','author')
    list_editable = ()
    # prepopulated_fields = {'slag': ('title, id')}
    list_filter = ('date',)


admin.site.register(Article, ArticleAdmin)

