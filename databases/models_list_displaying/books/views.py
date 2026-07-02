from datetime import date
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import Book
from django.http import HttpResponse


def parse_date(date_str: str) -> date:
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        raise ValidationError("Неверный формат даты. Используйте YYYY-MM-DD.")


def books_view(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


def books_by_date(request, date_str):
    target_date = parse_date(date_str)

    books = Book.objects.filter(pub_date=target_date)

    all_dates = (
        Book.objects.values_list("pub_date", flat=True)
        .distinct()
        .order_by("pub_date")
    )
    all_dates_list = list(all_dates)

    prev_date = next_date = None
    try:
        idx = all_dates_list.index(target_date)
        if idx > 0:
            prev_date = all_dates_list[idx - 1]
        if idx < len(all_dates_list) - 1:
            next_date = all_dates_list[idx + 1]
    except ValueError:
        # Даты нет в базе
        pass

    return render(
        request,
        'books/books_by_date.html',
        {
            'books': books,
            'current_date': target_date,
            'prev_date': prev_date,
            'next_date': next_date,
        },
    )

# def books_by_date(request, date_str):
#     return HttpResponse(f"<h1>Год</h1> {date_str}")
