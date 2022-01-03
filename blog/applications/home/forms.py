from django import forms
from django.db.models import fields


#Models
from .models import Contact, Suscribers

class SuscribersForm(forms.ModelForm):
    class Meta:
        model = Suscribers
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'placeholder': 'Correo Electronico'
                }
            )
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')