from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index)
]


def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")