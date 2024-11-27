from django.http import HttpResponse, QueryDict
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Main HOME page',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        "is_authenticated": True
    }    
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About page")