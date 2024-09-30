# shop/views.py
from django.shortcuts import render
from .models import Book, Author

def home(request):
    return render(request, 'shop/home.html')

# View to list all books
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'shop/book_list.html', {'books': books})

# View to list all authors
def author_list(request):
    authors = Author.objects.all()  # Fetch all authors from the database
    return render(request, 'shop/author_list.html', {'authors': authors})