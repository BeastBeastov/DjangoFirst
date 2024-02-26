from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .models import Article
from .forms import ArticleForm, LoginUserForm, ContactForm
from django.utils import timezone


# Create your views here.
def admin(request):
    return render(request, '/admin')


def logout_user(request):
    logout(request)
    return redirect('main')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "main/register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title='Регистрация')
        return context  # dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class ContactUser(FormView):
    form_class = ContactForm
    template_name = "main/contact.html"
    success_url = reverse_lazy("main")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title='Регистрация')
        return context  # dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('main')


class LoginUser(LoginView):
    form_clas = LoginUserForm
    template_name = "main/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title='Регистрация')
        return context #dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def articles(request):
    articles = Article.objects.order_by('-date')
    paginator = Paginator(articles, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/articles.html', {
        'title':'Все статьи на сайте',
        'articles': articles,
        'page_obj': page_obj,
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
        author = request.user
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        else:
            error = "Форма заполнена не верно"

    form = ArticleForm()
    context = {
        'form': form,
        'error': error,
        'user': request.user,
    }
    return render(request, 'main/create.html', context)
