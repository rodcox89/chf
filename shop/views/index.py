from django.conf import settings
import django.contrib.auth
from django.contrib.auth import authenticate, login, logout
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
import random
from django import forms
import homepage.models as hmod

templater = get_renderer('shop')

@view_function
def process_request(request):

  template_vars = {
  }


  # form = LoginForm()
  # if request.method == "POST":
  #     form = LoginForm(request.POST)
  #     if form.is_valid():
  #         #authenticate and login
  #         pass
  #
  # template_vars['form'] = form
  return HttpResponseRedirect('/shop/items/')




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



@view_function
def search(request):

    params = {}

    searchfor = request.REQUEST.get('input')
    print(searchfor)
    items = []
    if searchfor != '':
        if request.method == 'POST':
            items = hmod.Item.objects.filter(name = searchfor)
            print(items)
    else:
        items = hmod.Item.objects.all()


    params['items'] = items

    return templater.render_to_response(request, 'items.search.html', params)
