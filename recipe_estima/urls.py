from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.url_result, name='url_result'),
    path('list/', views.url_list, name='url_list'),
    path('recipe_detail/<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
    path('recipe_delete/<int:recipe_id>', views.recipe_delete, name='recipe_delete'),
    path('recipe_calorie/', views.recipe_calorie, name='recipe_calorie'),
]