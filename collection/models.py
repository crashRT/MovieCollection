from django.db import models

class collection(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField
    creator = models.TextField