from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
import random

templater = get_renderer('homepage')

@view_function
def process_request(request):
  params = {}
 	
  users = hmod.SiteUser.objects.all().order_by('last_name','first_name')
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
  	'first_name': user.first_name,
  	'last_name': user.last_name,
  	'email': user.email,
  })

  if request.method == 'POST':
  	form = UserEditForm(request.POST)
  	if form.is_valid():
  	  user.first_name = form.cleaned_data['first_name']
  	  user.last_name = form.cleaned_data['last_name']
  	  user.email = form.cleaned_data['email']
  	  user.save()
  	  return HttpResponseRedirect('/homepage/users/')


  params['form'] = form

  #user = hmod.SiteUser.objects.get(id=???)

  return templater.render_to_response(request, 'users.edit.html', params)  

class UserEditForm(forms.Form):
	first_name = forms.CharField(required=True, max_length=100)
	last_name = forms.CharField(required=True, max_length=100)
	email = forms.EmailField(required=True, max_length=100)