from django.urls import path
from books.views import books_view,books_by_date

urlpatterns = [
    path('books/', books_view, name='books'),
    path('books/<str:date_str>',books_by_date, name='books_by_date')

]
