from django.shortcuts import render

# Create your views here.


def blog(request):
    print("test")
    context = {
        'text': 'Hello blog! ',
        'title': 'Blog'
    }
    return render(
        request,
        'blog/index.html',
        context
        )


def exemplo(request):
    print('exemplo')
    context = {
        'text': 'Example',
        'title': 'Example'
    }
    return render(
        request,
        'blog/exemplo.html',
        context
        )
