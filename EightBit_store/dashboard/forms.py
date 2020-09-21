from django import forms
from dashboard.models import *

class CustomerForm(forms.ModelForm):
    class meta:
        model = Customer
        fields = ('firstname', 'lastname', 'contactNumber')

class ItemForm(forms.ModelForm):
    class meta:
        model = Item
        fields = ('_all_')

class OrderForm(forms.ModelForm):
    class meta:
        model = Order
        fields = ('_all_')

class CartForm(forms.ModelForm):
    class meta:
        model = Cart
        fields = ('_all_')

