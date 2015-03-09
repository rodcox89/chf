from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
import random
from django import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import homepage.models as hmod
from collections import OrderedDict

templater = get_renderer('shop')

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):

    template_vars = {}

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    template_vars = {}

        #shows the items in the shopping cart in a modal
    cart_items = {}# create a new dictionary
    cart_items = request.session['shopping_cart'] #assign session session to new  dictionary
    current_cart = {}
    for key,value in cart_items.items():


        item = hmod.Item.objects.get(id=key)
        ###############################create capsule############################### code
        item_container = [] #creates capsule
        item_container.append(item) #adds the item object
        item_container.append(value) #quantity
        ###############################capsule created############################### code

        current_cart[item.id] = item_container

    print('current_cart')
    print(current_cart)



    form = ShippingInfo()



    template_vars = {
        'form': form,
        'current_cart': current_cart,
	}







    return templater.render_to_response(request, 'checkout.html', template_vars)

class ShippingInfo(forms.Form):
    Address = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    City = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    State = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    Zip = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
