# Generated by Django 3.0.8 on 2020-07-31 18:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20200731_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='public_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 18, 0, 45, 332401, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]
