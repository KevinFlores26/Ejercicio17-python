from django.db import models

ACTIVITY_STATUS = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('R', 'Retired'),
        ('D', 'Died')
    )


class Genre(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128, null=False)
    summary = models.TextField(max_length=500, null=True, help_text='Escribe una descripción sobre la pelicula.')
    release_date = models.DateField(null=True, blank=True)
    budget = models.IntegerField(blank=True, null=True, default=100000000, help_text='Escribe el presupuesto usado en esta pelicula.')
    profits = models.IntegerField(blank=True, null=True, default=300000000, help_text='Escribe las ganancias de esta pelicula.')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Actor(models.Model):
    names = models.CharField(max_length=64, null=False)
    surnames = models.CharField(max_length=64, null=False)
    nacionality = models.CharField(max_length=32, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    status = models.CharField(max_length=8, choices=ACTIVITY_STATUS, default='A', blank=True,
                              help_text='Determinar el estado de actividad del actor.')

    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.names


class Director(models.Model):
    names = models.CharField(max_length=64, null=False)
    surnames = models.CharField(max_length=64, null=False)
    nacionality = models.CharField(max_length=32, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(default='', null=True, blank=True)
    status = models.CharField(max_length=1, choices=ACTIVITY_STATUS, default='A', blank=True,
                              help_text='Determinar el estado de actividad del director.')

    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.names


