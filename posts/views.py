from django.shortcuts import render, get_object_or_404
from .models import Post
from links.models import Link
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pub_date')
    links = Link.objects.order_by('title')
    return render(request, 'posts/index.html', {'posts': posts, 'links': links})

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/show.html', {'post': post})

def about(request):
    return render(request, 'posts/about.html')
