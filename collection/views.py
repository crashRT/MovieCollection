from django.shortcuts import render
from django.http import HttpResponse

def index(requested):
    return HttpResponse("Hello, world!")

