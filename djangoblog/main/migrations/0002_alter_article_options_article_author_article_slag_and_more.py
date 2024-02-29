# Generated by Django 5.0.2 on 2024-02-26 13:05

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор статьи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='slag',
            field=models.CharField(default='1', max_length=100, verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 13, 5, 33, 582919, tzinfo=datetime.timezone.utc), verbose_name='Время'),
        ),
    ]
