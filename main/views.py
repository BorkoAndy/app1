from django.http import HttpResponse, QueryDict
from django.shortcuts import render

from goods.models import Category


def index(request):       
    return render(request, 'main/index.html')     
                  

def about(request):
    return render(request, 'main/about.html')