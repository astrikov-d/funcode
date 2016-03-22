# coding: utf-8
from django.conf.urls import url
from django.http import HttpResponse

from .views import HomepageView

urlpatterns = [
    url(r'^', HomepageView.as_view(), name='homepage'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow:", content_type="text/plain")),
]
