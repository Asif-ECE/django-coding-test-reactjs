from django.forms import (BooleanField, CharField, CheckboxInput, DateInput,
                          ModelForm, Textarea, TextInput, forms)

from product.models import Product, Variant


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': "form-control", 'name': 'title'}),
            'variant': Textarea(attrs={'name': 'variant'}),
            'price_min': TextInput(attrs={'name': 'price_from'}),
            'price_max': TextInput(attrs={'name': 'price_to'}),
            'date': DateInput(attrs={'name': 'date'})
        }
