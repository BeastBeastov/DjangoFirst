# Generated by Django 4.1.7 on 2023-04-01 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('intro', models.CharField(max_length=300, verbose_name='Анонс')),
                ('text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Время')),
            ],
        ),
    ]
