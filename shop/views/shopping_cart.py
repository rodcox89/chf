from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
import random
from django import forms
import homepage.models as hmod

templater = get_renderer('shop')

@view_function
def process_request(request):
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







    template_vars['current_cart'] = current_cart




    return templater.render_to_response(request, 'shopping_cart.html', template_vars)







@view_function
def add(request):
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    iid =  request.urlparams[0]
    qty = int(request.urlparams[1])


    if iid in request.session['shopping_cart']:
        request.session['shopping_cart'][iid] += qty
        request.session.modified = True
        print(request.session['shopping_cart'])
    else:
        request.session['shopping_cart'][iid] = qty
        request.session.modified = True





    return HttpResponseRedirect('/shop/shopping_cart/')

@view_function
def delete(request):
    pid = request.urlparams[0]

    del request.session['shopping_cart'][pid]
    request.session.modified = True

    return HttpResponseRedirect('/shop/shopping_cart/')
