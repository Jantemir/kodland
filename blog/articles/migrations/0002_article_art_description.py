# Generated by Django 3.0.8 on 2020-07-30 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='art_description',
            field=models.TextField(default='default_description', verbose_name='Описание статьи'),
            preserve_default=False,
        ),
    ]