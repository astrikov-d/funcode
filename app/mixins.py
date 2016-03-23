# coding: utf-8
import json

from django.http import HttpResponse


class AjaxFormMixin(object):
    def process_data(self, data):
        raise NotImplementedError('Implement process_data method in your view.')

    def form_valid(self, form):
        self.process_data(form.cleaned_data)
        return HttpResponse(json.dumps({'result': 'success'}), content_type='application/json')

    def form_invalid(self, form):
        response = {
            'result': 'error',
            'errors': dict([(k, [e for e in v]) for k, v in form.errors.items()])
        }
        return HttpResponse(json.dumps(response), content_type='application/json')
