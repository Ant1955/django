from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('other', views.other, name='page3'),
    path('last', views.last, name='page4')
]

