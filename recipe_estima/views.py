from django.shortcuts import render, redirect, get_object_or_404
from .models import Url, Calorie
from bs4 import BeautifulSoup
import requests


def url_result(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if not Url.objects.filter(url=url).exists():
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            h1_tag = soup.find('h1', class_='recipe page-header')
            recipe_header = h1_tag.text.strip()
            div_ingredients = soup.find('div', class_='field field-name-field-ingredients field-type-text-long field-label-hidden')
            li_elements = div_ingredients.find_all('li')
            ingrid_elements = []
            for li in li_elements:
                element = li.text.strip()
                ingrid_elements.append(element)
            ingredients = ','.join(ingrid_elements)
            div_description = soup.find('div', class_='field field-name-field-preparation field-type-text-long field-label-above')
            li_elements_descr = div_description.find_all('li')
            descr_elements = []
            for li in li_elements_descr:
                element = li.text.strip()
                descr_elements.append(element)
            description = ','.join(descr_elements)
            Url.objects.create(url=url, recipe_header=recipe_header, ingredients=ingredients, description=description)
            recipe = Url.objects.filter(url=url).first()
            return redirect('recipe_estima:recipe_detail', recipe_id=recipe.id)
        else:
            return redirect('recipe_estima:home')


def url_list(request):
    urls = Url.objects.all()
    return render(request, 'url_list.html', {'urls': urls})


def recipe_detail(request, recipe_id):
    recipe = Url.objects.get(id=recipe_id)
    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(",")
    }
    return render(request, 'recipe_detail.html', context)


def recipe_delete(request, recipe_id):
    url = get_object_or_404(Url, pk=recipe_id)
    url.delete()
    return redirect('url_list')


def recipe_calorie(request):
    calories = Calorie.objects.all()
    context = {
        'calories': calories,
        'active_section': 'calorie_table'
    }
    return render(request, 'recipe_calorie.html', context)


def home(request):
    return render(request, 'recipe_estima/home.html')


def url_input(request):
    return render(request, 'url_input.html')
