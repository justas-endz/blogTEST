from django.contrib import admin
from .models import Article


class AdminArticles(admin.ModelAdmin):
    list_display = ('title', 'user', 'published', 'id')


admin.site.register(Article, AdminArticles)
