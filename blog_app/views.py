from django.shortcuts import render, get_object_or_404
from .models import Post


def showblog(request):
    post = Post.objects
    return render(request, 'blog_app/blog.html', {'post': post})


def specific_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog_app/specific_post.html', {'post': post})
