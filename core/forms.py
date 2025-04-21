from django import forms
from .models import ContactInquiry, SellRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'subject', 'contact_method', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number (Optional)'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'contact_method': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your Message'}),
        }
        def clean(self):
            cleaned_data = super().clean()
            contact_method = cleaned_data.get('contact_method')
            phone = cleaned_data.get('phone')
            if contact_method == 'phone' and not phone:
                raise forms.ValidationError("Phone number is required when contact method is Phone.")
            return cleaned_data 

class SellForm(forms.ModelForm):

    class Meta:
        model = SellRequest
        fields = ['name', 'email', 'phone', 'property_address', 'contact_method', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number (Optional)'}),
            'property_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Property Address'}),
            'contact_method': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your Message'}),
        }
        def clean(self):
            cleaned_data = super().clean()
            contact_method = cleaned_data.get('contact_method')
            phone = cleaned_data.get('phone')
            if contact_method == 'phone' and not phone:
                raise forms.ValidationError("Phone number is required when contact method is Phone.")
            return cleaned_data