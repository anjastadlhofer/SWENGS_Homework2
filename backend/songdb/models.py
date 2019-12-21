from django.db import models


class Country(models.Model):
    name = models.TextField()

    def __str__(self): return self.name


class Song(models.Model):
    CHOICES = (
        ('r', 'Rock'),
        ('p', 'Pop'),
        ('j', 'Jazz'),
        ('h', 'Hip Hop'),
        ('m', 'Metal')
    )

    title = models.TextField()
    genre = models.CharField(max_length=1, choices=CHOICES)
    release_date = models.DateField()
    story = models.TextField()
    selled = models.PositiveIntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    band = models.BooleanField()
    singers = models.ManyToManyField('Person', related_name="songs", blank=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    alias = models.TextField(null=True)
    active = models.BooleanField()
    year_of_birth = models.IntegerField()


    def __str__(self):
        return self.first_name + " " + self.last_name
