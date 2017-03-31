from .models import Blog
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html', {
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):   
    return render(request, 'view_post.html', {
        'posts': get_object_or_404(Blog, slug=slug)
    })
