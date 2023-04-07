
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.utils import timezone


# Create your views here.
def admin(request):
    return render(request, '/admin')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def articles(request):
    articles = Article.objects.order_by('-date')
    return render(request, 'main/articles.html', {
        'title':'Все статьи на сайте',
        'articles': articles,
    })


def detail(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'main/detail.html', {
        'title': article.title,
        'article': article,
    })


def delete(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect('articles')


def update(request, id):
    error = ''
    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
        'error': error,
        'id': id,
    }

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        else:
            error = "Форма заполнена не верно"

    return render(request, 'main/update.html', context)


def create(request):
    error = ''
    if request.method == "POST":
        article = Article()
        article.date = timezone.now()
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        else:
            error = "Форма заполнена не верно"

    form = ArticleForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
