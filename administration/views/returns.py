from django import forms
from django.forms import fields, util
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.core import validators
from django.core import exceptions
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod

templater = get_renderer('administrator')

@view_function
@login_required(login_url='/homepage/login/')
@permission_required('admin.delete_logentry', login_url='/homepage/login/')
def process_request(request):
    params = {}

    renters = hmod.Rentals.objects.all()

    params['renters'] = renters

    return templater.render_to_response(request, 'returns.html', params)

@view_function
def itemreturn(request):
    #initialize PARAMS
    params = {}

    #get return id from url passed through jquery
    rid = request.urlparams[0]

    #get item with same ID
    itemreturn = hmod.Rentals.objects.get(id=rid)

    #get user associated with rental
    userreturn = hmod.SiteUser.objects.get(id=itemreturn.person.id)

    #Initialize form so that we can edit it.
    form = ReturnItemForm(initial={
        'name': itemreturn.name,
        'rental_date': itemreturn.rental_date,
        'due_date': itemreturn.due_date,
        'new_damage': itemreturn.new_damage,
        'was_returned': itemreturn.was_returned,
    })

    #if a POST is called in the view
    if request.method == 'POST':
        form = ReturnItemForm(request.POST)
        if form.is_valid():
            #Reassign values
            itemreturn.name = form.cleaned_data['name']
            itemreturn.rental_date = form.cleaned_data['rental_date']
            itemreturn.due_date = form.cleaned_data['due_date']
            itemreturn.new_damage = form.cleaned_data['new_damage']
            itemreturn.was_returned = form.cleaned_data['was_returned']

            #save rental with updated information.
            itemreturn.save()

            #get late fee and damage fee from form
            latefee = form.cleaned_data['late_fee']
            damagefee = form.cleaned_data['damage_fee']

            #check for late fees and damage fees
            if latefee is None:
                latefee = 0
            if damagefee is None:
                damagefee = 0

            #tally up fees and add to user
            fee = latefee + damagefee
            userreturn.account_balance += fee

            #save user
            userreturn.save()

            return HttpResponseRedirect('/administrator/returns/')

    params['form'] = form
    params['rental'] = itemreturn
    return templater.render_to_response(request, 'returns.itemreturn.html', params)



class ReturnItemForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rental_date = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    due_date = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_damage = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    was_returned = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'was_returned'}))
    late_fee = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control fee', 'placeholder':'$0'}))
    damage_fee = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control fee','placeholder':'$0'}))
