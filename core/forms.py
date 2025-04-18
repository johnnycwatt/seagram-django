from django import forms
from .models import ContactInquiry, SellRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'message']

class SellForm(forms.ModelForm):
    class Meta:
        model = SellRequest
        fields = ['name', 'email', 'property_address', 'message']