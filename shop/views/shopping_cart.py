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

    template_vars = {}

        #shows the items in the shopping cart in a modal
    cart_items = {}
    final_cart = {}
    cart_items = request.session['shopping_cart']
    print('cart_items:')
    print(cart_items)

    for key,value in cart_items.items():

        item = hmod.Item.objects.get(id=key)
        name = item.name,
        print(name,'corresponds to ',len(value))










    return templater.render_to_response(request, 'shopping_cart.html', template_vars)







@view_function
def add(request):
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    iid = request.urlparams[0]
    qty = request.urlparams[1]
    print(iid)
    print(qty)
    print(request.session['shopping_cart'])

    if iid in request.session['shopping_cart']:
        request.session['shopping_cart'][iid] += qty
        request.session.modified = True
    else:
        request.session['shopping_cart'][iid] = qty
        request.session.modified = True

    template_vars = {
    }




    return HttpResponseRedirect('/shop/shopping_cart/')
