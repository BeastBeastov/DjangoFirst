
from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, ContactUser

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('articles', views.articles, name='articles'),
    path('create', views.create, name='create'),
    path('admin/', views.admin, name='admin'),
    path('logout', views.logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('contact/', ContactUser.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('update/<int:id>', views.update, name='update'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
]