from django.db import models

from pathlib import Path


class Book(models.Model):
    book_name = models.CharField(max_length=100, null=False, blank=False)
    page_count = models.IntegerField(null=True)
    category = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to=Path('images'))

    def __str__(self):
        return self.book_name
