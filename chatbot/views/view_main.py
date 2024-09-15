from django.http import HttpResponse
from django.shortcuts import render
from .view_context_search import search_context

def home(request):
    return render(request,"home.html")

