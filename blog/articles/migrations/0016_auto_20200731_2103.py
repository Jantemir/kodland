# Generated by Django 3.0.8 on 2020-07-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20200731_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='public_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
