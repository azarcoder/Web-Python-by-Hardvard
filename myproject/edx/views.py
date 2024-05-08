from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('This is index of edx')
def home(request):
    return HttpResponse('Home')
def greet(request, name):
    return render(request, 'edx/home.html', {
        'name' : name.capitalize()
    })
