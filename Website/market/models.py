from django.db import models


class Author(models.Model):
    name = models.CharField('Author', max_length=31)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Category(models.Model):
    name = models.CharField('Category', max_length=31)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Book(models.Model):
    cover_types = [('soft', 'Soft'), ('hard', 'Hard'), ('special', 'Special')]

    name = models.CharField('Book name', max_length=31)
    page_count = models.DecimalField('Numer of pages', max_digits=4, decimal_places=0)
    category = models.ManyToManyField('Category', verbose_name='Categories', limit_choices_to={'id__in': Category.objects.all()[:5]})
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True)
    price = models.DecimalField('Price', max_digits=4, decimal_places=2)
    cover_type = models.CharField('Cover type', max_length=31, choices=cover_types, blank=True, null=True)
    image = models.ImageField('Load image', upload_to='images/')

    def __str__(self):
        return f'{self.name}, {self.page_count} pages, {self.category}, written by {self.author_name}, {self.price}$'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
