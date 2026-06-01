from django.urls import path
from app.views import home_view,time_view,workdir_view,recipe_view


urlpatterns = [
    path('', home_view, name='home'),
    path('current_time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path('<str:dish>/', recipe_view, name='recipe')
]
