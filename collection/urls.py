from importlib.resources import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:movie_id>', views.detail, name='detail'),
    path('add', views.add, name='add'),
    path('edit/<int:movie_id>', views.edit, name='edit'),
    path('delete/<int:movie_id>', views.delete_movie, name='delete'),
    path('list/<str:tagname>', views.taglist, name='list'),
]