from django.shortcuts import render
from .models import Post


def showblog(request):
    post = Post.objects
    return render(request, 'blog_app/blog.html', {'post': post})
# Create your views here.
