from django.urls import path
from app.views import app

urlpatterns = [
    path('app/', app),
]
