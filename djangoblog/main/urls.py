
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('articles', views.articles, name='articles'),
    path('create', views.create, name='create'),
    path('admin', views.admin, name='admin'),
    path('update/<int:id>', views.update, name='update'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
]