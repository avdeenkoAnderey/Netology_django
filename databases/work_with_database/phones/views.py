from django.shortcuts import render, get_object_or_404
from .models import Phone

def show_catalog(request):
    sort_param = request.GET.get('sort', 'name')
    sort_mapping = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    ordering = sort_mapping.get(sort_param, 'name')
    phones = Phone.objects.all().order_by(ordering)
    context = {
        'phones': phones,
        'current_sort': sort_param
    }
    return render(request, 'phones/catalog.html', context)

def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, 'phones/product.html', context)
