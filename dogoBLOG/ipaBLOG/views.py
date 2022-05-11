from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Article


class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 5
    queryset = Article.objects.all().order_by('-published')
    template_name = 'index.html'


class PostDetailView(generic.DetailView):
    model = Article
    template_name = 'article.html'
