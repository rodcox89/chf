from django.core import validators
from django.core import exceptions
from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
import random

templater = get_renderer('administration')

@view_function
@permission_required('admin.delete_logentry', login_url='/homepage/login/')
def process_request(request):
  params = {}

  users = hmod.SiteUser.objects.filter(is_active=True).order_by('last_name','first_name')

  params['users'] = users # 44:06

  return templater.render_to_response(request, 'users.html', params)

################################
## Edit a user

@view_function
def edit(request):
  params = {}

  try:
    user = hmod.SiteUser.objects.get(id=request.urlparams[0])

  except hmod.SiteUser.DoesNotExist:
      return HttpResponseRedirect('/homepage/users/')

  form = UserEditForm(initial={
      'username': user.username,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'email': user.email,
  })

  if request.method == 'POST':
      form = UserEditForm(request.POST)
      form.userid = user.id
      if form.is_valid():
        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        return HttpResponseRedirect('/administration/users/')


  params['form'] = form

  #user = hmod.SiteUser.objects.get(id=???)

  return templater.render_to_response(request, 'users.edit.html', params)

class UserEditForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    def clean_username(self):
        user_count = hmod.SiteUser.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Username already exists.")
        return self.cleaned_data['username']
@view_function
def create(request):
    params = {}

    user = hmod.SiteUser()
    user.is_superuser = False
    user.save()

    return HttpResponseRedirect('/administration/users.edit/{}/'.format(user.id))

@view_function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/homepage/')

@view_function
def remove(request):

  try:
    user = hmod.SiteUser.objects.get(id=request.urlparams[0])

  except hmod.SiteUser.DoesNotExist:
    return HttpResponseRedirect('/administration/users/')

  user.is_active = False

  user.save()

  return HttpResponseRedirect('/administration/users/')
