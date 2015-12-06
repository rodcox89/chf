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
# @permission_required('admin.delete_logentry', login_url='/administration/login/')
def process_request(request):

  params = {}

  events = hmod.Event.objects.filter(is_active=True).order_by('name')

  params['events'] = events # 44:06

  return templater.render_to_response(request, 'events.html', params)

################################
## Edit a user

@view_function
def edit(request):
  params = {}

  try:
    event = hmod.Event.objects.get(id=request.urlparams[0])

  except hmod.Event.DoesNotExist:
    return HttpResponseRedirect('/homepage/events/')

  form = eventEditForm(initial={
      'name': event.name,
      'description': event.description,
      'location': event.location,
      'start_date': event.start_date,
      'end_date': event.end_date,
  })

  if request.method == 'POST':
      form = eventEditForm(request.POST)
      if form.is_valid():
        event.name = form.cleaned_data['name']
        event.description = form.cleaned_data['description']
        event.location = form.cleaned_data['location']
        event.start_date = form.cleaned_data['start_date']
        event.end_date = form.cleaned_data['end_date']
        event.save()
        return HttpResponseRedirect('/administration/events/')


  params['form'] = form

  #event = hmod.Events.objects.get(id=???)

  return templater.render_to_response(request, 'events.edit.html', params)

class eventEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    description = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    location = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    start_date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    end_date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))

@view_function
def create(request):
    params = {}

    event = hmod.Event()
    event.save()

    return HttpResponseRedirect('/administration/events.edit/{}/'.format(event.id))

@view_function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/homepage/')

@view_function
def remove(request):

  try:
    event = hmod.Event.objects.get(id=request.urlparams[0])

  except hmod.Event.DoesNotExist:
    return HttpResponseRedirect('/administration/events/')

  event.is_active = False

  event.save()

  return HttpResponseRedirect('/administration/events/')
