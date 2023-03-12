from django.db import models
from taggit.managers import TaggableManager


class collection(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField(null=True, blank=True)
    creator = models.ManyToManyField('creator', blank=True)
    discription = models.TextField(null=True, blank=True)
    tags = TaggableManager(blank=True)
    add_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class creator(models.Model):
    name = models.CharField(max_length=100)
    portfolio = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    vimeo = models.CharField(max_length=100, null=True, blank=True)
    software = TaggableManager(blank=True)
    memo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
