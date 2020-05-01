from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('klc/', views.klc, name='klc'),
    path('rjc/', views.rjc, name='rjc'),
]