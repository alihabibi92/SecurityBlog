from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.


def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    args = {'articles': articles}
    return render(request, 'articles/articleslist.html', args)


def articles_detail(request):
    return render(request, 'articles/articles_detail')