from django.db import models


class Recipe(models.Model):
    class Meta:
        app_label = 'recipe_estima'


class Calorie(models.Model):
    ingredient = models.CharField(max_length=100)
    calorie = models.IntegerField()

    def __str__(self):
        return self.ingredient


class Url(models.Model):
    url = models.URLField()
    recipe_header = models.CharField(max_length=50, default='Tytul Przepisu')
    ingredients = models.CharField(max_length=200, default='skladniki')
    description = models.CharField(max_length=2000, default='opis')
    calorie = models.ManyToManyField(Calorie)

    def __str__(self):
        return self.url


