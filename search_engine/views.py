from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def search(request):
    template = loader.get_template('search_engine/index.html')
    #template'search_engine/index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))