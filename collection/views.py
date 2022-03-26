from gc import collect
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.contrib.auth.models import User

from .models import collection
from .forms import add_movie

# ログイン用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('index'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'collection/login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))



@login_required
def index(requested):  
    collections = collection.objects.order_by('id')
    taglist = Tag.objects.all()
    context = {
        'movie_list':collections,
        'taglist':taglist,
    }
    return render(requested, 'collection/index.html', context)

@login_required
def taglist(requested, tagname):
    collections = collection.objects.filter(tags__name__in=[tagname]).distinct()
    taglist = Tag.objects.all()
    context = {
        'movie_list':collections,
        'taglist':taglist,
        'tagname':tagname,
    }
    return render(requested, 'collection/index.html', context)

@login_required
def creators(request):
    collections = collection.objects.order_by('creator').values_list('creator',flat=True).distinct()
    taglist = Tag.objects.all()
    context = {
        'collections':collections,
        'taglist':taglist,

    }
    return render(request, 'collection/creators.html', context)

@login_required
def creator_works(request, creator):
    works = collection.objects.filter(creator__icontains=creator).distinct()
    taglist = Tag.objects.all()
    context = {
        'movie_list':works,
        'taglist':taglist,
        'creator':creator,
    }
    return render(request, 'collection/index.html', context)

@login_required
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

@login_required
def add(request):
    if request.method == 'POST':
        form = add_movie(request.POST)
        newLink = form.data['link']
        if not collection.objects.filter(link = newLink).exists():
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            default_data = {'add_by':User.objects.get(pk=request.user.pk)}
            form = add_movie(default_data)
            taglist = Tag.objects.all()
            notice = 'その作品は既に登録されています'
            context = {
                'notice':notice,
                'form':form,
                'taglist':taglist,
            }
            return render(request, 'collection/form.html', context)

           
    else:
        default_data = {'add_by':User.objects.get(pk=request.user.pk)}
        form = add_movie(default_data)
        taglist = Tag.objects.all()
        context = {
            'form':form,
            'taglist':taglist,
        }
    return render(request, 'collection/form.html', context)

@login_required
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

@login_required
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
