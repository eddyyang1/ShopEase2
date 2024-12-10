# products/forms.py
from django import forms

class ProductSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label="Search Products")
