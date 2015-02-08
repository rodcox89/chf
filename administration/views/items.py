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
def process_request(request):
  params = {}

  items = hmod.Item.objects.filter(is_active=True).order_by('name')

  params['items'] = items # 44:06

  return templater.render_to_response(request, 'items.html', params)

################################
## Edit a user

@view_function
def edit(request):
  params = {}

  try:
    item = hmod.Item.objects.get(id=request.urlparams[0])

  except hmod.Item.DoesNotExist:
    return HttpResponseRedirect('/homepage/items/')

	# name = models.CharField(max_length=30)
	# description = models.CharField(max_length=144)
	# value = models.DecimalField(max_digits=6, decimal_places=2)
	# organization = models.CharField(max_length=144)
	# is_rentable = models.BooleanField(default=True)
	# is_active = models.NullBooleanField(default=True, blank=True, null=True)

  form = itemEditForm(initial={
      'name': item.name,
      'description': item.description,
      'value': item.value,
      'is_rentable': item.is_rentable,
  })

  if request.method == 'POST':
      form = itemEditForm(request.POST)
      if form.is_valid():
        item.name = form.cleaned_data['name']
        item.description = form.cleaned_data['description']
        item.value = form.cleaned_data['value']
        item.is_rentable = form.cleaned_data['is_rentable']
        item.save()
        return HttpResponseRedirect('/administration/items/')


  params['form'] = form

  #item = hmod.Items.objects.get(id=???)

  return templater.render_to_response(request, 'items.edit.html', params)

class itemEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    description = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    value = forms.DecimalField(required=True)
    is_rentable = forms.NullBooleanField(required=True)

@view_function
def create(request):
    params = {}

    item = hmod.Item()
    item.name = ''
    item.description = ''
    item.value = '0.0'
    item.save()

    return HttpResponseRedirect('/administration/items.edit/{}/'.format(item.id))

@view_function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/homepage/')

@view_function
def remove(request):

  try:
    item = hmod.Item.objects.get(id=request.urlparams[0])

  except hmod.Item.DoesNotExist:
    return HttpResponseRedirect('/administration/items/')

  item.is_active = False

  item.save()

  return HttpResponseRedirect('/administration/items/')
