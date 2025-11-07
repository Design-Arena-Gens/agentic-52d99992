from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/success/<str:code>/', views.register_success, name='register_success'),
    path('search/', views.search, name='search'),
    path('search/result/', views.search_result, name='search_result'),
]
