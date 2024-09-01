from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 200,
        'сыр, г': 300,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'lasagna': {
        'чеснок': 2,
        'пшеничная мука высшего сорта': 100,
        'морковь': 150,
        'молоко, литр': 1,
        'растительное масло ст. л.': 5,
        'репчатый лук, грамм': 150,
        'базилик, грамм': 20,
        'лазанья, штук': 12,
        'соль, чайная ложка': 1,
        'чёрный молотый перец, щепотки': 2,
        'мускатный орех, щепокти': 2,
        'томатный соус': 500,
        'говядина': 800,
        'томатная паста': 1,
        'сливочное масло 82,5': 150,
        'твёрдый сыр, грамм':  300
    }
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipe_view(request, dish):
    recipe = DATA.get(dish)
    if recipe:
        servings = request.GET.get('servings', 1)
        try:
            servings = int(servings)
            if servings < 1:
                raise ValueError("Количество порций должно быть положительным числом.")
        except ValueError:
            return HttpResponse("Некорректное значение для servings", content_type="text/plain")


        adjusted_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}


        context = {
            'recipe': adjusted_recipe,
            'dish': dish,
            'servings': servings,
        }
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse("Рецепт не найден", content_type="text/plain")