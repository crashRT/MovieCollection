from django.db import models
from taggit.managers import TaggableManager

class collection(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField(null=True, blank=True)
    creator = models.CharField(max_length=100, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title