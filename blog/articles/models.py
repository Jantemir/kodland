from django.db import models
from datetime import datetime
from django.utils import timezone
class Article(models.Model):
    art_title = models.CharField('Название статьи', max_length = 200, default = '')
    art_text = models.TextField('Текст статьи', default = '')
    art_description = models.TextField('Описание статьи', default = '')
    public_date = models.DateTimeField('Дата публикации')
    art_pic = models.CharField('Путь к картинке на сервере', max_length = 200, default = '')



