from django.shortcuts import render
# Create your views here.


def home(request):
    print('Home')

    return render(
        request,
        'home/index.html',
        {
            'text': 'We are in home',
            'title': 'Home'
        }
        )
