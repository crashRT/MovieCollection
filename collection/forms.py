from os import link
from tabnanny import check
from tkinter.ttk import LabeledScale
from .models import collection
from django import forms
from django.core.exceptions import ValidationError


class add_movie(forms.ModelForm):
    class Meta:
        model = collection
        fields = ('title', 'link', 'creator', 'discription', 'tags')
        labels = {
            'title': 'タイトル',
            'link': '埋め込みリンク',
            'creator': '映像作家',
            'discription': '概要',
            'tags': 'タグ,'
        }

        def clean(self):
            all_clean_data = super().clean()
            newLink = all_clean_data['link']
            if collection.objects.filter(link = newLink).count()>1:
                raise forms.ValidationError('入力した映像は既に登録済みです。')
