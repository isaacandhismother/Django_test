from django.shortcuts import render
from django.http import JsonResponse
from .models import Book


def index(request):
    return render(request, 'market/market_home.html')


def return_json(request):
    data = list(Book.objects.values())
    return JsonResponse(data, safe=False)
