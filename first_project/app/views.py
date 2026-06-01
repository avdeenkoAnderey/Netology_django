from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    try:
        files = os.listdir('.')
        files_list = '\n'.join(files)
        return HttpResponse(files_list)
    except Exception as e:
        return HttpResponse(f'Ошибка при получении списка файлов: {str(e)}')


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
}

def recipe_view(request, dish):
    # Получаем рецепт для указанного блюда, если его нет — возвращаем пустой словарь
    recipe_data = DATA.get(dish, {})
    
    # Если блюдо не найдено, возвращаем сообщение об ошибке
    if not recipe_data:
        return HttpResponse(f'Рецепт для "{dish}" не найден', status=404)
    
    # Получаем параметр servings из GET‑запроса, по умолчанию — 1
    servings_str = request.GET.get('servings')
    
    if servings_str:
        try:
            # Конвертируем в целое число
            servings = int(servings_str)
            # Если число отрицательное или ноль, используем 1
            if servings <= 0:
                servings = 1
        except ValueError:
            # В случае ошибки конвертации используем 1 порцию
            servings = 1
    else:
        # Если параметр servings не передан, используем 1 порцию
        servings = 1
    
    # Умножаем количество ингредиентов на число порций и формируем строки для ответа
    recipe_lines = []
    for ingredient, amount in recipe_data.items():
        total_amount = amount * servings
        recipe_lines.append(f'{ingredient}: {total_amount}')
    
    # Объединяем строки в один текст с переносами строк
    response_text = '\n'.join(recipe_lines)
    
    # Возвращаем текстовый ответ
    return HttpResponse(response_text, content_type='text/plain; charset=utf-8')
