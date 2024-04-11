from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookStore.as_view(), name='home'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book-info')
]
