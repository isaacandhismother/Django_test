from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BookStore.as_view(), name='home')
]
