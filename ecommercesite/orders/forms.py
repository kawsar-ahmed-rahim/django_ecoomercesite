from django import forms
from .models import Order


class orderCreateForm(forms.ModelFrom):
    class Meta:
        model = Order
        fields = ["full_name", "email", "address"]