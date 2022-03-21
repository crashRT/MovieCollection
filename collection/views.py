from gc import collect
from multiprocessing import context
from operator import methodcaller
from sqlite3 import paramstyle
from tempfile import tempdir
from django.shortcuts import get_object_or_404, redirect, render
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
    if request.method == 'POST':
        form = add_movie(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = add_movie()
    return render(request, 'collection/form.html', {'form':form})

