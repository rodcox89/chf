from django.conf import settings
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
  return templater.render_to_response(request, 'index.html', template_vars)




@view_function
def loginform(request):

  template_vars = {
  }

  form = LoginForm()
  if request.method == "POST":
      form = LoginForm(request.POST)
      if form.is_valid():
          #authenticate and login
          return HttpResponse('''
          <script>
            window.location.href = window.location.href;
          </script>

          ''')

  template_vars['form'] = form
  return templater.render_to_response(request, 'index.loginform.html', template_vars)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()




# @view_function
# def check_username(request):
#   name = request.REQUEST.get('username')
#
#   user = hmod.SiteUser.objects.filter(username=name)
#   print(user)
#   print(name)
#
#   if len(user)==0:
#       print('ohhh baby')
#       return HttpResponse('good')
#
#
#   # if user is None:
#   #     return HttpResponse('You can use this username')
#   #
#   # elif username == hmod.SiteUser.object.get(username==username):
#   #     return HttpResponse('username already in use')
#
#
#   return HttpResponse('hey world')
