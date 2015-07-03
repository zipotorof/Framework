#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from forum.models import PostCategorie, PostSsCategorie, Post, PostMessage, Thread

def home(request):
    categories = PostCategorie.objects.all()
    sscategories = PostSsCategorie.objects.all()
    posts = Post.objects.order_by('-date')[:5]
    return render(request, 'forum/index.html', locals())

def list_posts(request, cat):
    mycat = PostSsCategorie.objects.get(id=cat)
    posts = Post.objects.filter(categorie=cat).order_by('-date')
    return render(request, 'forum/list_posts.html', locals())

def post(request, p):
    post = Post.objects.get(id=p)
    message = PostMessage.objects.filter(post=p)
    thread = Thread.objects.all()
    return render(request, 'forum/post.html', locals())

def list_posts_bysscat(request, categorie, sscategorie):
    return render(request, 'forum/list_posts.html') 

def add_post(request):
    return render(request, 'forum/new.html')
