# Generated by Django 5.0.3 on 2024-04-11 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_book_author_alter_book_book_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]
