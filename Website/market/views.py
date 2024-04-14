from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Book


class BookStore(ListView):
    paginate_by = 4
    model = Book
    template_name = 'market/market_home.html'
    context_object_name = 'book_store'
    extra_context = {'title': 'Home page'}

    def get_queryset(self):
        queryset = super().get_queryset()
        for book in queryset:
            book.categories = book.category.all()
            book.num_categories = book.category.count()
        return queryset


class BookDetailView(DetailView):
    model = Book
    template_name = 'market/book_page.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['categories'] = book.category.all()
        return context


def index(request):
    return render(request, 'market/market_home.html')
