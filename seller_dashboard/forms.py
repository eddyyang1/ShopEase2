# seller_dashboard/forms.py
from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']  # Include the image field

    # Customize the form if necessary
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False  # Make the image field optional
