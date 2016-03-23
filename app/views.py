# coding: utf-8
from django.views.generic import FormView

from .classes import Keeper
from .forms import PaymentForm
from .mixins import AjaxFormMixin
from .models import AppUser


class HomepageView(AjaxFormMixin, FormView):
    template_name = 'homepage.html'
    form_class = PaymentForm

    @staticmethod
    def get_class_children():
        for i in xrange(1, 4):
            Keeper()
        return Keeper.get_instances()

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['class_children'] = self.get_class_children()
        return context

    def process_data(self, data):
        user, receivers, amount = data['user'], data['receivers'], data['amount']

        if receivers:
            part = amount / float(len(receivers))
            user.change_balance(-amount)

            receivers = AppUser.objects.filter(inn__in=receivers)
            for receiver in receivers:
                receiver.change_balance(part)
