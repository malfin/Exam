import random

from django.shortcuts import render

from mainapp.models import Group


def index(request):
    group = Group.objects.all()
    number = random.choice(group)
    context = {
        'title': 'главная',
        'number': number,
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    context = {
        'title': 'о нас',
    }
    return render(request, 'mainapp/about.html', context)
