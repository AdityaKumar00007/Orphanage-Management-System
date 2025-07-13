# orphanage/forms.py
from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor_name', 'email', 'phone', 'donation_type', 'amount']
        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'donation_type': forms.Select(attrs={'class': 'form-control', 'id': 'id_donation_type'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Donation Amount'}),
        }
