# coding: utf-8
from django.views.generic import TemplateView

from .classes import Keeper


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    @staticmethod
    def get_class_children():
        for i in xrange(1, 4):
            Keeper()
        return Keeper.get_instances()

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['class_children'] = self.get_class_children()
        return context