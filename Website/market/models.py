from django.db import models


class Book(models.Model):
    name = models.CharField('Book name', max_length=31)
    page_count = models.DecimalField('Numer of pages', max_digits=4, decimal_places=0)
    category = models.CharField('Category', max_length=31)
    author_name = models.CharField('Author', max_length=31)
    price = models.DecimalField('Price', max_digits=4, decimal_places=2)
    image = models.ImageField('Load image')

    def __str__(self):
        return f'{self.name}, {self.page_count} pages, {self.category}, written by {self.author_name}, {self.price}$'