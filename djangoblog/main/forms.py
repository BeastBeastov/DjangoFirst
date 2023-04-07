from .models import Article
from django.forms import ModelForm, TextInput, Textarea


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


