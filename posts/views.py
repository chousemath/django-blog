from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def index(request):
    posts = models.Post.objects.order_by('-pub_date')
    return render(request, 'posts/index.html', {'posts': posts})

def show(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, 'posts/show.html', {'post': post})

def about(request):
    return render(request, 'posts/about.html')
