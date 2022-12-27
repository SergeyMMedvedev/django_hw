from django.shortcuts import render
from django.http import HttpResponseNotFound


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def get_ingredients(request, dish):
    ingredients = DATA.get(dish, {}).copy()
    if not ingredients:
        return HttpResponseNotFound("Dish not founded")
    context = {}
    servings = request.GET.get('servings', 0)
    if servings:
        if servings.isdigit():
            for k, v in ingredients.items():
                ingredients[k] = v * int(servings)
    context['recipe'] = ingredients
    return render(request, 'calculator/index.html', context)
