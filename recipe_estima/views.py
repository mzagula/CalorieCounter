from django.shortcuts import render, redirect, get_object_or_404
from .models import Url


def url_input(request):
    return render(request, 'url_input.html')


def url_result(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if not Url.objects.filter(url=url).exists():
            Url.objects.create(url=url)
            recipe = Url.objects.get(url=url)
            context = {
                'recipe': recipe
            }
            return render(request, 'recipe_detail.html', context)
    else:
        return redirect('url_input')


def url_list(request):
    urls = Url.objects.all()
    return render(request, 'url_list.html', {'urls': urls})


def recipe_detail(request, recipe_id):
    recipe = Url.objects.get(id=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)


def recipe_delete(request, recipe_id):
    url = get_object_or_404(Url, pk=recipe_id)
    url.delete()
    return redirect('url_list')

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
