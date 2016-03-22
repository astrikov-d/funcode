# coding: utf-8
from django import forms
from django.core.exceptions import ValidationError

from .models import AppUser
from .validators import validate_inn


class PaymentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=AppUser.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    receivers = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    amount = forms.DecimalField(max_digits=16, decimal_places=2,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_receivers(self):
        receivers = self.cleaned_data.get('receivers')
        if not all([validate_inn(receiver) for receiver in receivers.split(',')]):
            raise ValidationError('Invalid INN')
        return receivers
