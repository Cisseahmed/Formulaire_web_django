from .models import Contact
from django import forms


class Contact_lists(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'nom',
            'prenom',
            'numero',
            'email',
        ]

        widgets = {'numero':forms.NumberInput}