from django.http import HttpResponse
from django.shortcuts import render
from .view_context_search import search_context
import json
import os

def home(request):
    current_dir=os.path.realpath(os.path.dirname(__file__))
    json_path=os.path.join(current_dir,'lang.json')
    with open(json_path, 'r') as f:
        lang_data=json.loads(f.read())
    languages=lang_data
    return render(request,"home.html",context={"languages":languages})

