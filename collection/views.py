from gc import collect
from multiprocessing import context
from operator import methodcaller
from tempfile import tempdir
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import collection
from .forms import add_movie

def index(requested):  
    collections = collection.objects.order_by('id')
    context = {
        'movie_list':collections
    }
    return render(requested, 'collection/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(collection, pk=movie_id)
    return render(request, 'collection/detail.html', {'movie':movie})

def form(request):
    form = add_movie()
    context = {'form':form}
    render(request, 'collection/form.html', context)

