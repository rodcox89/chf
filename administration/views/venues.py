from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from bootstrap3_datetime.widgets import DateTimePicker
import homepage.models as hmod
import random

templater = get_renderer('administration')

@view_function
@permission_required('admin.delete_logentry', login_url='/administration/login/')
@permission_required('homepage.add_event', login_url='/administration/login/')
def process_request(request):
  params = {}

  venues = hmod.Venue.objects.filter(is_active=True).order_by('name')

  params['venues'] = venues # 44:06

  return templater.render_to_response(request, 'venues.html', params)

################################

	# name = models.CharField(max_length=30)
	# description = models.CharField(max_length=255)
	# address = models.CharField(max_length=30)
	# city = models.CharField(max_length=30, blank=True, null=True)
	# state = models.CharField(max_length=30, blank=True, null=True)
	# zip_code = models.IntegerField(max_length=5, blank=True, null=True)


@view_function
def edit(request):
  params = {}

  try:
    venue = hmod.Venue.objects.get(id=request.urlparams[0])

  except hmod.Venue.DoesNotExist:
    return HttpResponseRedirect('/homepage/venues/')



  form = venueEditForm(initial={
      'name': venue.name,
      'description': venue.description,
      'address': venue.address,
      'city': venue.city,
      'state': venue.state,
      'zip_code': venue.zip_code,
  })

  if request.method == 'POST':
      form = venueEditForm(request.POST)
      if form.is_valid():
        venue.name = form.cleaned_data['name']
        venue.description = form.cleaned_data['description']
        venue.address = form.cleaned_data['address']
        venue.city = form.cleaned_data['city']
        venue.city = form.cleaned_data['state']
        venue.zip_code = form.cleaned_data['zip_code']
        venue.save()
        return HttpResponseRedirect('/administration/venues/')


  params['form'] = form

  #venue = hmod.Venues.objects.get(id=???)

  return templater.render_to_response(request, 'venues.edit.html', params)

class venueEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    description = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    address = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    city = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    state = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    zip_code = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))

@view_function
def create(request):
    params = {}

    venue = hmod.Venue()
    venue.name = ''
    venue.description = ''
    venue.save()

    return HttpResponseRedirect('/administration/venues.edit/{}/'.format(venue.id))

@view_function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/homepage/')

@view_function
def remove(request):

  try:
    venue = hmod.Venue.objects.get(id=request.urlparams[0])

  except hmod.Venue.DoesNotExist:
    return HttpResponseRedirect('/administration/venues/')

  venue.is_active = False

  venue.save()

  return HttpResponseRedirect('/administration/venues/')
