from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('articles/<int:pk>', views.PostDetailView.as_view(), name='articles'),
]