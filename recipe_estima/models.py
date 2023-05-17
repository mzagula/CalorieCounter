from django.db import models

class Recipe(models.Model):
    class Meta:
        app_label = 'recipe_estima'


class Url(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


#     title = models.CharField(max_length=200)
#     instructions = models.TextField()
#     servings = models.IntegerField()
#     image_url = models.URLField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
# class Ingredient(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     quantity = models.FloatField()
#     unit = models.CharField(max_length=20)
#     calories_per_unit = models.FloatField()
