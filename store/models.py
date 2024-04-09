from django.db import models

from pathlib import Path


class Book(models.Model):
    book_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Book Name')
    page_count = models.IntegerField(null=True, verbose_name='Page Count')
    category = models.CharField(max_length=100, null=False, blank=False, verbose_name='Category')
    author = models.CharField(max_length=100, null=True, verbose_name='Author')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, verbose_name='Price')
    image = models.ImageField(null=True, blank=True, upload_to=Path('images'), verbose_name='Image')

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

