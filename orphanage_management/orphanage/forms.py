# orphanage/forms.py
from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor_name', 'email', 'amount']  # Include relevant fields
        widgets = {
            'donor_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Donation Amount'}),
        }
