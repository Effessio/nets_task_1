#coding: utf-8
import urllib
import urllib2
import json
from django.shortcuts import render

from django.views.generic import TemplateView


class MyView(TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('code', ''):
            code = self.request.GET.get('code', '')
            client_id = '11469ea1eda4432dfad8'
            client_secret = '0843cbd06d27b481e34f0dcddc05085776d21409'
            post_data = [
                ('code', code),
                ('client_id', client_id),
                ('client_secret', client_secret)]
            result = urllib2.urlopen('https://github.com/login/oauth/access_token', urllib.urlencode(post_data))
            token_string = result.read()

            rs = urllib2.urlopen('https://api.github.com/user/repos?'+token_string)
            js = json.loads(rs.read())
            return render(request, self.template_name, {'js':js})
        else:
            return render(request, self.template_name)

