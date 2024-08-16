from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html',{'caption':"DzenCat"})


def new(request):
    data = {
        'caption':"Cat Number 2"
    }
    return render(request, 'main/new.html',data)
def other(request):
    return render(request, 'main/other.html',{'caption':"3th Cat"})
def last(request):
    return render(request, 'main/last.html',{'caption':"Cat last"})