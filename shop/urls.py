# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for the root URL
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
]