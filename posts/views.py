from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    posts = models.Post.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {'posts': posts})
