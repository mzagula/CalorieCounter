from django.urls import path
# from .views import recipe_detail
from . import views

urlpatterns = [
    path('', views.url_input, name='url_input'),
    path('result/', views.url_result, name='url_result'),
    path('list/', views.url_list, name='url_list'),
    path('recipe_detail/<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
]