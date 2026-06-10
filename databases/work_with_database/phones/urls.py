from django.contrib import admin
from django.urls import path
from phones.views import show_catalog,show_product


urlpatterns = [
    path('catalog/', show_catalog),
    path('catalog/<slug:slug>/', show_product),
]