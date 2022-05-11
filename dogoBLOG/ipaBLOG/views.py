from django.views import generic
from .models import Article, Comment
from django.shortcuts import redirect, render
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} Taken!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'e-mail {email} exists!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Check passwords!')
            return redirect('register')
    return render(request, 'register.html')


class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 5
    queryset = Article.objects.all().order_by('-published')
    template_name = 'index.html'


class PostDetailView(generic.DetailView):
    model = Article
    template_name = 'article.html'
