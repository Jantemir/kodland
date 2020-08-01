from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.full_text, name = 'full_text'),
    path('form_to_create/', views.form_to_create, name = 'form_to_create'),
    path('create_article/', views.create_article, name = 'create_article'),
]

