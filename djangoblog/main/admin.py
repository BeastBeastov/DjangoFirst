from django.contrib import admin
from .models import Article
from django.utils import timezone


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_link = ('id', 'title', 'date')
    search_fields = ('title', 'article')
    # prepopulated_fields = {'slag': ('title, id')}
    list_filter = ('date',)


admin.site.register(Article, ArticleAdmin)

