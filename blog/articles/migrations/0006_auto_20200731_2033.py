# Generated by Django 3.0.8 on 2020-07-31 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200731_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='public_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 20, 33, 35, 839362), verbose_name='Дата публикации'),
        ),
    ]