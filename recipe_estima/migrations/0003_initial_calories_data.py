from django.db import migrations

def add_initial_calories(apps, schema_editor):
    Calorie = apps.get_model('recipe_estima', 'Calorie')
    initial_data = [
        # Meat
        {'ingredient': 'Chicken Breast', 'calorie': 165},
        {'ingredient': 'Beef (lean)', 'calorie': 250},
        {'ingredient': 'Pork Chop', 'calorie': 242},
        {'ingredient': 'Salmon', 'calorie': 208},
        
        # Vegetables
        {'ingredient': 'Carrot', 'calorie': 41},
        {'ingredient': 'Broccoli', 'calorie': 34},
        {'ingredient': 'Potato', 'calorie': 77},
        {'ingredient': 'Tomato', 'calorie': 18},
        
        # Fruits
        {'ingredient': 'Apple', 'calorie': 52},
        {'ingredient': 'Banana', 'calorie': 89},
        {'ingredient': 'Orange', 'calorie': 47},
        {'ingredient': 'Strawberries', 'calorie': 32},
        
        # Dairy
        {'ingredient': 'Milk (3.5%)', 'calorie': 64},
        {'ingredient': 'Cheese (Cheddar)', 'calorie': 402},
        {'ingredient': 'Yogurt (plain)', 'calorie': 61},
        {'ingredient': 'Eggs', 'calorie': 155},
        
        # Grains
        {'ingredient': 'Rice (white)', 'calorie': 130},
        {'ingredient': 'Bread (wheat)', 'calorie': 265},
        {'ingredient': 'Pasta', 'calorie': 131},
        {'ingredient': 'Oatmeal', 'calorie': 389},
        
        # Snacks
        {'ingredient': 'Chocolate (dark)', 'calorie': 546},
        {'ingredient': 'Nuts (mixed)', 'calorie': 607},
        {'ingredient': 'Potato Chips', 'calorie': 536},
        {'ingredient': 'Popcorn', 'calorie': 387},
    ]
    
    for data in initial_data:
        Calorie.objects.create(**data)

def remove_calories(apps, schema_editor):
    Calorie = apps.get_model('recipe_estima', 'Calorie')
    Calorie.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('recipe_estima', '0002_calorie_url_description_url_ingredients_and_more'),
    ]

    operations = [
        migrations.RunPython(add_initial_calories, remove_calories),
    ] 