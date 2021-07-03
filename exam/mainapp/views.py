from django.shortcuts import render


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    context = {
        'title': 'о нас',
    }
    return render(request, 'mainapp/about.html', context)
