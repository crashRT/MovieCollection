from tkinter.ttk import LabeledScale
from .models import collection
from django import forms

class add_movie(forms.ModelForm):
    class Meta:
        model = collection
        fields = ('title', 'link','creator', 'discription', 'tags')
        labels = {
            'title':'タイトル',
            'link':'埋め込みリンク',
            'creator':'映像作家',
            'discription':'概要',
            'tags':'タグ',
        }