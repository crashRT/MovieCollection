from importlib.resources import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:movie_id>', views.detail, name='detail'),
    path('form', views.form, name='form'),
]