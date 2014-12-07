from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import MyView


urlpatterns = [
    url(r'', MyView.as_view()),
]
