from django.urls import path,register_converter
from books.views import books_view,books_by_date
from books import converters


register_converter(converters.PubDateConverter, "date_str")


urlpatterns = [
    path('books/', books_view, name='books'),
    path('books/<str:date_str>/',books_by_date, name='books_by_date'),
]