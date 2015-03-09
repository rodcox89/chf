from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
from datetime import datetime
from django import forms

import random

templater = get_renderer('homepage')

@view_function
def process_request(request):
  template_vars = {
  }
  return templater.render_to_response(request, 'index.html', template_vars)


@view_function
def loginform(request):
    template_vars = {}

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request,user)

            return HttpResponse('''
            <script>
                window.location.href = window.location.href;
            </script>
            ''')


    template_vars['form'] = form
    return templater.render_to_response(request, 'index.loginform.html', template_vars)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):

        user = authenticate(username=self.cleaned_data.get('username', ''), password=self.cleaned_data.get('password', ''))
        if user == None:
            raise forms.ValidationError("Username/password is not valid")
        return self.cleaned_data
