from django.shortcuts import get_object_or_404, render

from .models import Post


def home(request):
    posts = Post.objects.filter(published=True)
    return render(request, "core/index.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, "core/detail.html", {"post": post})
