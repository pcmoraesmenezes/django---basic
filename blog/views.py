from django.shortcuts import render
from blog.data_ import posts

# Create your views here.


def blog(request):
    context = {
        'text': 'Hello blog! ',
        'title': 'Blog',
        'posts': posts

    }
    return render(
        request,
        'blog/index.html',
        context
        )


def post(request, id):
    context = {
        'posts': posts

    }
    return render(
        request,
        'blog/index.html',
        context
        )


def exemplo(request):
    context = {
        'text': 'Example',
        'title': 'Example',
    }
    return render(
        request,
        'blog/exemplo.html',
        context
        )
