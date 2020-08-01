# Generated by Django 3.0.8 on 2020-07-31 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_art_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_description',
            field=models.TextField(default='', verbose_name='Описание статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_pic',
            field=models.CharField(default='', max_length=200, verbose_name='Путь к картинке на сервере'),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_text',
            field=models.TextField(default='', verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_title',
            field=models.CharField(default='', max_length=100, verbose_name='Название статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='public_date',
            field=models.DateTimeField(default='', verbose_name='Дата публикации'),
        ),
    ]
