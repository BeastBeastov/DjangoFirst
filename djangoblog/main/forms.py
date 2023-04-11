from .views import AuthenticationForm
from .models import Article
from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput, Form, EmailField
from captcha.fields import CaptchaField


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'intro', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статьи',
                'spellcheck': 'True'
            }),
            'intro': Textarea(attrs={
                'class': 'form-control',
                'rows': '2',
                'placeholder': 'Введите анонс статьи',
                'spellcheck': 'True'

            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'rows': '7',
                'placeholder': 'Введите текст статьи',
                'spellcheck': 'True'
            }),
        }

class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class' : 'form-control'}))
    username = CharField(label='Пароль', widget=PasswordInput(attrs={'class' : 'form-control'}))


class ContactForm(Form):
    name = CharField(label='Имя', max_length=255)
    email = EmailField(label='Email')
    message = CharField(widget=Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
