from django.shortcuts import render
from django.shortcuts import render

# Create your views here.


def search(request):
    render(request,'/search_engine/index.html')