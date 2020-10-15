from datetime import date

from django.db import models


class Category(models.Model):

    name = models.CharField('Category', max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):

    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'


class Genre(models.Model):

    name = models.CharField('Genre', max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):

    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField('Release year', default=2020)
    coutry = models.CharField(max_length=30)
    directors = models.ManyToManyField(Actor, related_name='film_director')
    actors = models.ManyToManyField(Actor, related_name='film_actor')
    genres = models.ManyToManyField(Genre)
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text='In USD')
    fess_in_world = models.PositiveIntegerField(default=0, help_text='In USD')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Movie:
        verbose_name = 'Movie shot'
        verbose_name_plural = 'Movie shots'


class RatingStar(models.Model):

    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating star'
        verbose_name_plural = 'Rating stars'


class Rating(models.Model):

    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Review(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

