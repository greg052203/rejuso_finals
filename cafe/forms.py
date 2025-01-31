from django import forms
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'quantity']
        widgets = {
            'item': forms.Select(attrs={'onchange': 'updatePrice()'}),
        }

class CustomUserCreationForm(UserCreationForm):
    is_superuser = forms.BooleanField(required=False, label="Register as Superuser")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']
