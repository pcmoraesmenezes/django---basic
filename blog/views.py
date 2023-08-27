from django.shortcuts import render
from blog.data_ import posts
from django.http import Http404
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


def post(request, post_id):

    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    if found_post is None:
        raise Http404('Not find Post')

    context = {
        'post': found_post,
        'title': found_post['title']

    }
    return render(
        request,
        'blog/post.html',
        context
        )


def exemplo(request):
    context = {
        'text': 'Example',
        'title': 'Example',
    }
    return render(
        request,
        'blog/index.html',
        context
        )
