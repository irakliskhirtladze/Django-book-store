from django import forms
from .models import Author, Category


class BookFilterForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label='All Authors', required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='All Categories', required=False)
