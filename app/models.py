# coding: utf-8
from decimal import Decimal

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class AppUser(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    email = models.EmailField()

    balance = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Balance, RUB', default=0)
    inn = models.CharField(max_length=10, verbose_name='INN')

    def can_be_charged(self, amount):
        return self.balance >= amount

    def change_balance(self, amount):
        if amount < 0 and not self.can_be_charged(amount * -1):
            return

        self.balance += Decimal(amount)
        self.save(update_fields=['balance'])
        return self.balance

    def __unicode__(self):
        return u'%s [%s]' % (self.email, self.inn)
