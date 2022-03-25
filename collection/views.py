from gc import collect
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from taggit.models import Tag

from .models import collection
from .forms import add_movie

def index(requested):  
    collections = collection.objects.order_by('id')
    taglist = Tag.objects.all()
    context = {
        'movie_list':collections,
        'taglist':taglist,
    }
    return render(requested, 'collection/index.html', context)

def taglist(requested, tagname):
    collections = collection.objects.filter(tags__name__in=[tagname]).distinct()
    taglist = Tag.objects.all()
    context = {
        'movie_list':collections,
        'taglist':taglist,
        'tagname':tagname,
    }
    return render(requested, 'collection/index.html', context)

def creators(request):
    collections = collection.objects.order_by('creator').values_list('creator',flat=True).distinct()
    taglist = Tag.objects.all()
    context = {
        'collections':collections,
        'taglist':taglist,

    }
    return render(request, 'collection/creators.html', context)

def creator_works(request, creator):
    works = collection.objects.filter(creator__icontains=creator).distinct()
    taglist = Tag.objects.all()
    context = {
        'movie_list':works,
        'taglist':taglist,
        'creator':creator,
    }
    return render(request, 'collection/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(collection, pk=movie_id)
    taglist = Tag.objects.all()
    tags = movie.tags.all()
    context = {
        'movie':movie,
        'taglist':taglist,
        'tags':tags,
    }
    return render(request, 'collection/detail.html', context)

def add(request):
    if request.method == 'POST':
        form = add_movie(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = add_movie()
        taglist = Tag.objects.all()
        context = {
            'form':form,
            'taglist':taglist,
        }
    return render(request, 'collection/form.html', context)

def edit(request, movie_id):
    info = get_object_or_404(collection, pk=movie_id)
    if request.method == 'POST':
        form = add_movie(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = add_movie(instance=info)
        taglist = Tag.objects.all()
        context = {
            'form':form,
            'taglist':taglist,
        }
 
    return render(request, 'collection/edit.html', context)

def delete_conf(request, movie_id):
    movie = get_object_or_404(collection, pk=movie_id)
    context = {
        'movie':movie,
    }
    return render(request, 'collection/delete.html', context)

@require_POST
def delete_movie(request, movie_id):
    info = get_object_or_404(collection, pk=movie_id)
    info.delete()
    return redirect('index')
