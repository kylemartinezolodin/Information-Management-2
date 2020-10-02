from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('firstname', 'lastname', 'contactNumber', 'email')

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('__all__')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('__all__')

