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
import datetime
from django.core.mail import send_mail, EmailMessage
from django.core.validators import validate_email
from datetime import timedelta

templater = get_renderer('administration')

@view_function
# @permission_required('admin.delete_logentry', login_url='/administration/login/')
def process_request(request):
    params = {}

    #Filters items by is active
    items = hmod.Item.objects.filter(is_active=True).order_by('name')
    params['items'] = items # 44:06

    #rental list
    rentals = []

    #for loop that filters available items
    for item in items:
        if item.is_available == False:
          rental = hmod.Rental.objects.get(name=item)
          print('###############################rental############################### coderental')
          print(rental)
          print(rental.name)
          rentals.append(rental)

    rentals = []

    #filters all overdue items
    overdue_items = hmod.Rental.objects.filter(was_returned=False)

    #overdue lists
    thirties = []
    sixties = []
    nineties = []
    under = []

    #gets overdue dates
    ninety = datetime.date.today()-datetime.timedelta(days=90)
    sixty = datetime.date.today()-datetime.timedelta(days=60)
    thirty = datetime.date.today()-datetime.timedelta(days=30)

    #for loop that filters items by due date
    for item in overdue_items:
        print('in for loop')
        if item.due_date < ninety:
          print('###############################more than 90############################### code')
          print(item.due_date)
          nineties.append(item)


        elif item.due_date < sixty:
          print('###############################more than 60############################### code')
          print(item.due_date)
          sixties.append(item)

        elif item.due_date < thirty:
          print('###############################more than 30############################### code')
          print(item.due_date)
          thirties.append(item)

        else:
          print('###############################it was less than 30############################### code')
          print(item.due_date)
          under.append(item)

    #lists that get passed to the items.html view
    params['thirties'] = thirties
    params['sixties'] = sixties
    params['nineties'] = nineties
    params['under'] = under
    params['rentals'] = rentals
    params['overdue_items'] = overdue_items


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


@view_function
def return_item(request):

  try:
    rental = hmod.Rental.objects.get(id=request.urlparams[0])

  except hmod.Rental.DoesNotExist:
    return HttpResponseRedirect('/administration/items/')




  # rental = hmod.Rental.objects.get(name=item)
  # print('###############################Rentals############################### code')
  # print(rental.name)
  # print(rental.customer)
  #


  return HttpResponseRedirect('/administration/item.itemreturn.html/')

@view_function
def return_rental(request):
  params = {}
  print('###############################return rental view function############################### code')
  try:
    rental = hmod.Rental.objects.get(id=request.urlparams[0])
    item_name = rental.name

    item = hmod.Item.objects.get(name=item_name)
    print(rental)
    print(item)

  except hmod.Rental.DoesNotExist:
    return HttpResponseRedirect('/homepage/items/')

  # for r in rental:
  #   if item.is_available == False:
  #
  #     print('###############################rental############################### coderental')
  #     print(rental)
  #     print(rental.name)
  #     rentals.append(rental)


  # form = RentalReturnForm()
  form = RentalReturnForm(initial={
    'Waive Late Fee': rental.waive_late,
    'New Damage': rental.damage,
    'Damage Fee': rental.damage_fee,
    'Waive Damage': rental.waive_damage,
  })

  if request.method == 'POST':
      form = RentalReturnForm(request.POST)
      print('###############################request was post############################### code')
      if form.is_valid():

        print('###############################form was valid############################### code')
        rental.waive_late = form.cleaned_data['waive_late']
        rental.new_damage = form.cleaned_data['new_damage']
        rental.damage_fee = form.cleaned_data['damage_fee']
        rental.waive_damage = form.cleaned_data['waive_damage']
        rental.was_returned = True
        rental.save()
        item = hmod.Item.objects.get(name=rental.name)
        item.is_available = True
        item.save()
        return HttpResponseRedirect('/administration/items/')


  params['rental'] = rental
  params['form'] = form
  # params['item'] = item
  print('###############################params############################### code')
  print(params)


  #item = hmod.Items.objects.get(id=???)

  return templater.render_to_response(request, 'items.itemreturn.html', params)

class RentalReturnForm(forms.Form):
  waive_late = forms.BooleanField(required=False)
  new_damage = forms.CharField(required=False, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
  damage_fee = forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
  waive_damage = forms.BooleanField(required=False)
class ReturnItemForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rental_date = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    due_date = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_damage = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    was_returned = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'was_returned'}))
    late_fee = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control fee', 'placeholder':'$0'}))
    damage_fee = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control fee','placeholder':'$0'}))


@view_function
def sendmail(request):
    print('Nigga we made it!')
    #empty params dictionary
    params = {}

    #get url paramater
    batch = request.urlparams[0]

    #create empty email list
    email_batch = []

    #gets overdue dates depending on time
    ninety = datetime.date.today()-datetime.timedelta(days=90)
    sixty = datetime.date.today()-datetime.timedelta(days=60)
    thirty = datetime.date.today()-datetime.timedelta(days=30)

    #check batch we want to send
    if batch == '30':
        print('-----------------> 30!')
        overdue_thirty = hmod.Rental.objects.filter(due_date__range=(sixty, thirty))
        for rental in overdue_thirty:
            email = rental.customer.email
            email_batch.append(email)

    if batch == '60':
        print('-----------------> 60!')
        overdue_sixty = hmod.Rental.objects.filter(due_date__range=(ninety, sixty))
        for rental in overdue_sixty:
            email = rental.customer.email
            email_batch.append(email)

    if batch == '90':
        print('-----------------> 90!')
        overdue_ninety = hmod.Rental.objects.filter(due_date__lt=(ninety))
        for rental in overdue_ninety:
            email = rental.customer.email
            email_batch.append(email)

    #Send emails based on lists
    message = templater.render(request, 'email_reminder.html', params)
    subject = 'Item Overdue!'
    to = email_batch
    from_email = 'rodcox89@gmail.com'
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    #return items page
    return HttpResponseRedirect('/administrator/items/')
