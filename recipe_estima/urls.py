from django.urls import path
# from .views import recipe_detail
from . import views

urlpatterns = [
    path('', views.url_input, name='url_input'),
    path('result/', views.url_result, name='url_result'),
]