from gc import collect
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import collection
from .forms import add_movie

def index(requested):  
    collections = collection.objects.order_by('id')
    context = {
        'movie_list':collections
    }
    return render(requested, 'collection/index.html', context)

def taglist(requested, tagname):
    collections = collection.objects.filter(tags__name__in=[tagname]).distinct()
    context = {
        'movie_list':collections
    }
    return render(requested, 'collection/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(collection, pk=movie_id)
    return render(request, 'collection/detail.html', {'movie':movie})

def add(request):
    if request.method == 'POST':
        form = add_movie(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = add_movie()
    return render(request, 'collection/form.html', {'form':form})

def edit(request, movie_id):
    info = get_object_or_404(collection, pk=movie_id)
    if request.method == 'POST':
        form = add_movie(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = add_movie(instance=info)
    return render(request, 'collection/edit.html', {'form':form})

@require_POST
def delete_movie(request, movie_id):
    info = get_object_or_404(collection, pk=movie_id)
    info.delete()
    return redirect('index')
