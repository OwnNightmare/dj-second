from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

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
    'paradise':
        {
        'Мука пшеничная, г': 90,
        'Сахар, г': 80,
        'Соль, щепотка': 1,
        'Цедра лимона, ч. л.': 1,
        'Яйца куриные, шт.': 3,
        'Фрукты, г': 330,
        'Желе для тортов, г': 5,
        'Киви, г': 1,
        'Клубника свежая, г': 4,
        'Мед из шиповника ст.л.': 1
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


def recipes_view(request: WSGIRequest):
    given_servings: str = request.GET.get('servings', '1')
    copied_data = {}
    for dish, ingrs in DATA.items():
        copied_data[dish] = {}
        for ingr, amount in ingrs.items():
            if given_servings.isdigit():
                servings = int(given_servings)
                copied_data[dish][ingr] = amount * servings
            else:
                copied_data[dish][ingr] = amount
                return HttpResponse('Убедитесь, что количество порций является целым числом')
    if request.path == '/omlet/':
        context = {'dish': 'омлет', 'recipe': copied_data['omlet']}
        return render(request, 'calculator/index.html', context)
    elif request.path == '/pasta/':
        context = {'dish': 'паста', 'recipe': copied_data['pasta']}
        return render(request, 'calculator/index.html', context)
    elif request.path == '/buter/':
        context = {'dish': 'бутерброд обыкновенный', 'recipe': copied_data['buter']}
        return render(request, 'calculator/index.html', context)
    elif request.path == '/paradise/':
        context = {'dish': 'фруктовый рай', 'dish_type': 'торт',  'recipe': copied_data['paradise']}
        return render(request, 'calculator/index.html', context)
