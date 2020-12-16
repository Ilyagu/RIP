from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Anime
from .models import Description


def index(request):
    anime_list = Anime.objects.all()
    context = {'anime_list': anime_list}
    return render(request, 'shop/index.html', context)


def detail(request, anime_id):
    anime_list = Anime.objects.all()
    for i in anime_list:
        if i.id == anime_id:
            anime = i
    description = get_object_or_404(Description, pk=anime_id)
    return render(request, 'shop/detail.html', {'anime': anime, 'description': description})