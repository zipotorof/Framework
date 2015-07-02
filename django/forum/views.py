#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from forum.models import PostCategorie, PostSsCategorie

def home(request):
    categories = PostCategorie.objects.all()
    sscategories = PostSsCategorie.objects.all()
    return render(request, 'forum/index.html', locals())

def list_posts(request, categorie):
    return render(request, 'forum/list_posts.html')

def list_posts_bysscat(request, categorie, sscategorie):
    return render(request, 'forum/list_posts.html') 

def add_post(request):
    return render(request, 'forum/new.html')
