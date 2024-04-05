from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'page_count', 'author_name', 'price')
    search_fields = ['name', 'category', 'author_name']


admin.site.register(Book, BookAdmin)
