from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('index/', views.memory_list, name='index'),
    path('memory/<int:pk>/', views.memory_detail, name='memory_detail'),
    path('klc/', views.klc, name='klc'),
    path('rjc/', views.rjc, name='rjc'),
    path('lac/', views.lac, name='lac'),
]