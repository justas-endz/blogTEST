from django.contrib import admin
from .models import Article, Comment


class AdminArticles(admin.ModelAdmin):
    list_display = ('title', 'user', 'published', 'id')


@admin.register(Comment)
class AdminComments(admin.ModelAdmin):
    list_display = ('post', 'publish_date', 'commenting_user', 'content')
    model = Comment


admin.site.register(Article, AdminArticles)
