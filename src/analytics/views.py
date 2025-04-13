from django.shortcuts import render
from django.db.models import Count
from library.models import Book, Author, Category
from .models import BookView, CategoryAnalytics, AuthorAnalytics

def analytics_dashboard(request):
    top_books = Book.objects.annotate(view_count=Count('views')).order_by('-view_count')[:5]
    top_authors = Author.objects.annotate(book_count=Count('books')).order_by('-book_count')[:5]
    top_categories = Category.objects.annotate(book_count=Count('books')).order_by('-book_count')[:5]

    context = {
        'top_books': top_books,
        'top_authors': top_authors,
        'top_categories': top_categories
    }
    return render(request, 'analytics/dashboard.html', context)
