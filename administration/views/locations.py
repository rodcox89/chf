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
# @permission_required('admin.delete_logentry', login_url='/administration/login/')
def process_request(request):
  params = {}

  locations = hmod.Location.objects.filter(is_active=True).order_by('name')

  params['locations'] = locations # 44:06

  return templater.render_to_response(request, 'locations.html', params)

################################
## Edit a user

@view_function
def edit(request):
  params = {}

  try:
    location = hmod.Location.objects.get(id=request.urlparams[0])

  except hmod.Location.DoesNotExist:
    return HttpResponseRedirect('/homepage/locations/')

  form = locationEditForm(initial={
      'name': location.name,
      'description': location.description,
      'city': location.city,
      'state': location.state,
  })

  if request.method == 'POST':
      form = locationEditForm(request.POST)
      if form.is_valid():
        location.name = form.cleaned_data['name']
        location.description = form.cleaned_data['description']
        location.city = form.cleaned_data['city']
        location.state = form.cleaned_data['state']
        location.save()
        return HttpResponseRedirect('/administration/locations/')


  params['form'] = form

  #location = hmod.locations.objects.get(id=???)

  return templater.render_to_response(request, 'locations.edit.html', params)

class locationEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    description = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}))
    state = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))


@view_function
def create(request):
    params = {}

    location = hmod.Location()
    location.save()

    return HttpResponseRedirect('/administration/locations.edit/{}/'.format(location.id))

@view_function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/homepage/')

@view_function
def remove(request):

  try:
    location = hmod.Location.objects.get(id=request.urlparams[0])

  except hmod.Location.DoesNotExist:
    return HttpResponseRedirect('/administration/locations/')

  location.is_active = False

  location.save()

  return HttpResponseRedirect('/administration/locations/')
