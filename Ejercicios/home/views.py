from django.shortcuts import render, redirect, get_object_or_404

from .models import *

def index(request):
    actors = Actor.objects.all()
    directors = Director.objects.all()
    genres = Genre.objects.all()
    movies = Movie.objects.all()

    if request.method == 'POST':
        if 'id_director' in request.POST:
            return redirect('movies_director')

    return render(
        request,
        'index.html',
        context={
            'actors': actors,
            'directors': directors,
            'genres': genres,
            'movies': movies
        }
    )


def movies(request):
    actors = Actor.objects.all()
    directors = Director.objects.all()
    genres = Genre.objects.all()
    movies = Movie.objects.all()

    return render(
        request,
        'movies.html',
        context={
            'actors': actors,
            'directors': directors,
            'genres': genres,
            'movies': movies
        }
    )


def movies_director(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    genres = Genre.objects.all()
    movies = director.movies.all()

    return render(
        request,
        'movies_director.html',
        context={
            'director': director,
            'genres': genres,
            'movies': movies
        }
    )


def movies_actor(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    genres = Genre.objects.all()
    movies = actor.movies.all()

    return render(
        request,
        'movies_actor.html',
        context={
            'actor': actor,
            'genres': genres,
            'movies': movies
        }
    )

