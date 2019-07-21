from django.db import models
import datetime

# Create your models here.
class Country(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=30)
    landmark = models.CharField(max_length=30)
    pincode = models.IntegerField()

    class Meta:
        db_table = "country_Info"

class Actor(models.Model):
    aname = models.CharField(max_length=50)
    aage = models.IntegerField()
    aexperience = models.IntegerField()
    anoOfMovies = models.IntegerField()
    aaddress = models.CharField(max_length=50)

    class Meta:
        db_table = "actor_Info"

class Director(models.Model):
    dname = models.CharField(max_length=50)
    dage = models.IntegerField()
    dexperience = models.IntegerField()
    dnoOfMovies = models.IntegerField()
    daddress = models.CharField(max_length=50)
    class Meta:
        db_table = "director_Info"

class Movie(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    noSongs = models.CharField(max_length=50)
    releasedate = models.DateField(default=datetime.date.today)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    class Meta:
        db_table = "movie_Info"
