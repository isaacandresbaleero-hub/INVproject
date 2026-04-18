from django import forms 
from .models import product

#define a form
class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"
        labels = {
            'product_id': 'product ID',
            'name': 'name',
            'sku': 'sku',
            'price': 'price',
            'quantity': 'quantity',
            'supplier': 'supplier name',

        }

        widgets = {
            'product_id' : forms.NumberInput(
                attrs={'placeholder': 'e.g 1', 'class': 'form-control'}
            ),

            'name' : forms.TextInput(
                attrs={'placeholder': 'shirt', 'class': 'form-control'}
            ),

            'sku' : forms.TextInput(
                attrs={'placeholder': 'e.g &1234', 'class': 'form-control'}
            ),
            'price' : forms.NumberInput(
                attrs={'placeholder': 'e.g 19.99', 'class': 'form-control'}
            ),

            'quantity' : forms.NumberInput(
                attrs={'placeholder': 'e.g 10', 'class': 'form-control'}
            ),
            'supplier' : forms.TextInput(
                attrs={'placeholder': 'e.g riham', 'class': 'form-control'}
            )
            

        }