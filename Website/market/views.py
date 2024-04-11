from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Book


class BookStore(ListView):
    paginate_by = 4
    model = Book
    template_name = 'market/market_home.html'
    context_object_name = 'book_store'
    extra_context = {'title': 'Home page'}


def index(request):
    return render(request, 'market/market_home.html')


def return_json(request):
    data = list(Book.objects.values())
    return JsonResponse(data, safe=False)
