from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.return_json),
    path('home/', views.index)
]
