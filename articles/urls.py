from django.contrib import admin
from django.urls import path
from . import views


app_name = "articles"
urlpatterns = [
    path('', views.articles_list, name='list'),

]