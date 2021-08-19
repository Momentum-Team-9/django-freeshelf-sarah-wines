from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author, User, Category

# Create your views here.
def list_books(request):
    # books = Book.objects.all()
    books = Book.objects.all().order_by('-created_at')
    return render(request, "books/list_books.html",
                  {"books": books})

def index(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect('list_books')
    return render(request, 'books/index.html', {'users': users})

def show_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(
        request,
        "books/show_book.html",
        {"book": book, "pk": pk},
    )
def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()

    return render(request, "books/show_category.html", {"category": category, "books": books})