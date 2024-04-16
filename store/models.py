from django.db import models
from django.utils.translation import gettext_lazy as _

from pathlib import Path
from store.choices import CoverChoices


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name=_('Author'))
    category = models.ManyToManyField('Category', verbose_name=_('Category'))
    book_name = models.CharField(max_length=100, verbose_name=_('Book Name'))
    page_count = models.IntegerField(null=True, blank=True, verbose_name=_('Page Count'))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(null=True, blank=True, upload_to=Path('images'), verbose_name=_('Image'))
    book_cover = models.CharField(max_length=15, choices=CoverChoices.choices,
                                  blank=True, null=True, verbose_name=_('Book Cover'))

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Author(models.Model):
    author_name = models.CharField(max_length=100, verbose_name=_('Author Name'))

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name=_('Category Name'))

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
