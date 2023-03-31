from django.urls import re_path, include, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies_director/<int:director_id>/', views.movies_director, name='movies_director'),
    path('movies_actor/<int:actor_id>/', views.movies_actor, name='movies_actor')
]
