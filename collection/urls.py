from importlib.resources import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:movie_id>', views.detail, name='detail'),
    path('add', views.add, name='add'),
    path('edit/<int:movie_id>', views.edit, name='edit'),
    path('delete/<int:movie_id>', views.delete_movie, name='delete'),
    path('list/tag=<str:tagname>', views.taglist, name='taglist'),
    path('creators', views.creators, name='creators'),
    path('list/creator=<str:creator>', views.creator_works, name='works'),
    path('delete_conf', views.delete_conf, name='delete_conf'),
    path('login', views.Login, name='Login'),
    path("logout", views.Logout, name="Logout"),
]