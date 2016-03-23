# coding: utf-8
from django import forms
from django.core.exceptions import ValidationError

from .helpers import clean_inn
from .models import AppUser
from .validators import validate_inn


class PaymentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=AppUser.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    receivers = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    amount = forms.DecimalField(max_digits=16, decimal_places=2, min_value=0.01,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        data = self.cleaned_data
        user = data.get('user')
        amount = data.get('amount')
        receivers = data.get('receivers')

        if user:
            if not user.can_be_charged(amount):
                raise ValidationError('User do not have enough balance')
            if user.inn in receivers:
                raise ValidationError('User can not send payment to himself')

        return data

    def clean_receivers(self):
        receivers = self.cleaned_data.get('receivers').split(',')
        if not all([validate_inn(receiver) for receiver in receivers]):
            raise ValidationError('Invalid INN')

        for receiver in receivers:
            if not AppUser.objects.filter(inn=clean_inn(receiver)).exists():
                raise ValidationError('User with specified INN: %s not found in the database' % receiver)

        return [clean_inn(receiver) for receiver in receivers]
