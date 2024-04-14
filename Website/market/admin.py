from django.contrib import admin

# არ ვიცი როგორ მივუთითო ისე, რომ ჩანდეს რომელი აპიდან ვაიმპორტებ
# from Website.market.models import Book, Category, Author - ვცედე, არ იმუშავა :/
from .models import Book, Category, Author


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class CategoryInline(admin.TabularInline):
    model = Book.category.through
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_books')
    inlines = [BookInline]
    search_fields = ['name']

    def display_books(self, obj):
        return ", ".join([book.name for book in Book.objects.filter(author_name=obj)])
    display_books.short_description = 'Books'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_books')
    search_fields = ['name']
    inlines = [CategoryInline]

    def get_inline_instances(self, request, obj=None):
        if obj:
            return [CategoryInline(self.model, self.admin_site)]
        return []

    def get_books(self, obj):
        return ", ".join([book.name for book in obj.book_set.all()])

    get_books.short_description = 'Books'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_categories', 'page_count', 'author_name', 'price')
    search_fields = ['name', 'category__name', 'author_name']

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    get_categories.short_description = 'Categories'

