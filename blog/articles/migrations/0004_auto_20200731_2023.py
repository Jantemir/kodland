# Generated by Django 3.0.8 on 2020-07-31 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200731_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='public_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации'),
        ),
    ]
