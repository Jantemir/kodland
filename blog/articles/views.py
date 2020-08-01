from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article
from django.urls import reverse
import psycopg2
from datetime import datetime
from django.core.files.storage import FileSystemStorage


def index(request):
    latest_articles = Article.objects.order_by('-public_date')[:10]
    return render(request, 'articles/main_page.html', {'art_list' : latest_articles})

def full_text(request, article_id):
    try:
        art = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена...')
    return render(request, 'articles/full_text.html', {'article' : art})

def form_to_create(request):
    return render(request, 'articles/form_to_create.html')

def create_article(request):
    data = request.POST
    image = request.FILES["docfile"]
    image_name = data['title'] + '.jpg'
    fs = FileSystemStorage()
    fs.save(image_name, image)
    url = fs.url(image_name)
    art = Article(art_title = data['title'], art_text = data['text'], art_description=data['descr'], public_date = datetime.now(), art_pic = url)
    art.save()
    return HttpResponseRedirect(reverse('articles:index'))
