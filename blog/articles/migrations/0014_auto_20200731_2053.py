# Generated by Django 3.0.8 on 2020-07-31 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20200731_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='public_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 20, 53, 36, 960750), verbose_name='Дата публикации'),
        ),
    ]
