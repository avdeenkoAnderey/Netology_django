from django.contrib import admin
from django.urls import path
from phones.views import show_catalog,show_product


app_name = 'phones'  # пространство имён

urlpatterns = [
    path('catalog/', show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', show_product, name='product'),
]