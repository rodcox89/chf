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

  products = hmod.Product.objects.filter(is_active=True).order_by('name')

  params['products'] = products # 44:06

  return templater.render_to_response(request, 'products.html', params)

################################
## Edit a user
# class Product(models.Model):
# 	name = models.CharField(max_length=30)
# 	description = models.CharField(max_length=144)
# 	category = models.CharField(max_length=144)
# 	current_price = models.DecimalField(max_digits=6,decimal_places=2)


@view_function
def edit(request):
  params = {}

  try:
    product = hmod.Product.objects.get(id=request.urlparams[0])

  except hmod.Product.DoesNotExist:
    return HttpResponseRedirect('/homepage/products/')



  form = productEditForm(initial={
      'name': product.name,
      'description': product.description,
      'category': product.category,
      'current_price': product.current_price,
  })

  if request.method == 'POST':
      form = productEditForm(request.POST)
      if form.is_valid():
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.category = form.cleaned_data['category']
        product.current_price = form.cleaned_data['current_price']
        product.save()
        return HttpResponseRedirect('/administration/products/')


  params['form'] = form

  #product = hmod.Products.objects.get(id=???)

  return templater.render_to_response(request, 'products.edit.html', params)

class productEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    description = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    category = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    current_price = forms.DecimalField(required=True)

@view_function
def create(request):
    params = {}

    product = hmod.Product()
    product.name = ''
    product.description = ''
    product.value = '0.0'
    product.save()

    return HttpResponseRedirect('/administration/products.edit/{}/'.format(product.id))

@view_function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/homepage/')

@view_function
def remove(request):

  try:
    product = hmod.Product.objects.get(id=request.urlparams[0])

  except hmod.Product.DoesNotExist:
    return HttpResponseRedirect('/administration/products/')

  product.is_active = False

  product.save()

  return HttpResponseRedirect('/administration/products/')
