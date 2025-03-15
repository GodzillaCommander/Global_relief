from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('donate/normal/', views.adhd, name="adhd"),
    path('donate/', views.donate, name='donate'),
    path('donate/normal/todo/', views.todo, name='todo'),
]