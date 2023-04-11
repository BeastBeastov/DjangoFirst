from django.db import models
from django.utils import timezone


class Article(models.Model):
    id = models.AutoField('id', primary_key=True)
    title = models.CharField('Заголовок', max_length=100, null=False)
    intro = models.CharField('Анонс', max_length=300, null=False)
    text = models.TextField('Статья', null=False)
    #slag = models.CharField('slug', null=False)
    date = models.DateTimeField('Время', default=timezone.now())
    #author = models.ForeignKey('Автор статьи')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


