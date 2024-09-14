from django.http import HttpResponse
from django.shortcuts import render
from .view_context_search import search_context

def home(request):
    if request.method=="POST":
        query=request.POST.get("message")
        reply=search_context(query)
        print(reply)
        context={"message":reply[0]}
    else:
        context={
        }
    return render(request,"home.html",context)

