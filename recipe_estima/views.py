from django.shortcuts import render, redirect
# from .models import Recipe, Ingredient
from .models import Url


def url_input(request):
    return render(request, 'url_input.html')

def url_result(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        Url.objects.create(url=url)  # Zapisz adres URL do bazy danych
        return render(request, 'url_result.html', {'url': url})
    else:
        return redirect('url_input')


# def recipe_detail(request, recipe_id):
#     recipe = Recipe.objects.get(id=recipe_id)
#     ingredients = Ingredient.objects.filter(recipe=recipe)
#     total_calories = sum(i.calories_per_unit * i.quantity for i in ingredients)
#     context = {
#         'recipe': recipe,
#         'ingredients': ingredients,
#         'total_calories': total_calories,
#     }
#     return render(request, 'recipe_detail.html', context)
