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
from django.core.mail import send_mail, EmailMessage
from django.core.validators import validate_email
import homepage.models as hmod
import requests
import datetime
from collections import OrderedDict

templater = get_renderer('shop')

def get_total(request):
    product_total =0
    rental_total =0

    total=0
    if 'shopping_cart' in request.session:

        product_ids = request.session['shopping_cart']
        for key,value in product_ids.items():
            product = hmod.Product.objects.get(id=key)
            amount = int(product.current_price)

            total += (value*amount)
            print('###############################total############################### code')
            print(total)

    if 'rental_cart' in request.session:
        print("rental runs")
        rental_ids = request.session['rental_cart']
        for itemid in rental_ids:
            item = hmod.Item.objects.get(id=itemid)
            amount = int(item.rental_price*30)
            print("this is the ", amount)
            total += (amount)
            print(total)




    return total


@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):

    template_vars = {}

    ###############################here you will check to see if request method is post###############################
    checkout_form = CheckoutForm()
    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():

            API_KEY = '042b5f481e6f7261ee92269cdb40c412'

            request.session['chargedict'] = {
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': get_total(request),
                'type': 'Visa',
                'number': checkout_form.cleaned_data['CardNumber'],
                'exp_month': checkout_form.cleaned_data['ExpirationMonth'],
                'exp_year': checkout_form.cleaned_data['ExpirationYear'],
                'cvc': checkout_form.cleaned_data['Cvv'],
                'name': checkout_form.cleaned_data['Name'] ,
                'description': 'Charge at the CHF foundation',

            }






            return HttpResponseRedirect('/shop/checkout.charge/')





    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}


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

    if 'rental_cart' not in request.session:# checks for rental session
        request.session['rental_cart'] = []# if no rental session, it get's created


    rental_ids = request.session['rental_cart'] # rental ids adopts all of the rental session attributes
    rental_cart = [] ## creates an empty list
    for rental_item in rental_ids:  #iterates through the rental session

        rental_item = hmod.Item.objects.get(id=rental_item) #checks id's against the Id's of actual items in my database
        rental_cart.append(rental_item) # adds the actual item objects to the rental cart list I made





    template_vars = {

        'current_cart': current_cart,
        'checkout_form': checkout_form,
        'rental_cart': rental_cart,
	}







    return templater.render_to_response(request, 'checkout.html', template_vars)


@view_function
@login_required(login_url='/homepage/login/')
def charge(request):

    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = '042b5f481e6f7261ee92269cdb40c412'


    r = requests.post(API_URL, data=request.session['chargedict'])



    resp = r.json()
    print(resp)

    if 'error' in resp:
        print("ERROR: ", resp['error'])



    else:
        template_vars={}

        request.session['response'] = resp
        template_vars['confirmation'] = resp
        print('###############################confirmation###############################')
        print(resp)


        print(template_vars)

        if 'shopping_cart' not in request.session:
            request.session['shopping_cart'] = {}





            #shows the items in the shopping cart in a modal
        cart_items = request.session['shopping_cart'] #assign session session to new  dictionary

        current_cart = {}
        for key,value in cart_items.items():


            item = hmod.Product.objects.get(id=key)
            ###############################create capsule############################### code
            item_container = [] #creates capsule
            item_container.append(item) #adds the item object
            item_container.append(value) #quantity
            ###############################capsule created############################### code

            current_cart[item.id] = item_container
            purch = hmod.Purchase()

            purch.customer = request.user
            purch.total = 45
            purch.purchase_date = datetime.date.today()
            purch.charge_id = resp["ID"]


            print(purch)

        if 'rental_cart' not in request.session:# checks for rental session
            request.session['rental_cart'] = []# if no rental session, it get's created


        rental_ids = request.session['rental_cart'] # rental ids adopts all of the rental session attributes
        rental_cart = [] ## creates an empty list
        for rental_item in rental_ids:  #iterates through the rental session

            rentitem = hmod.Item.objects.get(id=rental_item) #checks id's against the Id's of actual items in my database
            rental_cart.append(rentitem) # adds the actual item objects to the rental cart list I made
            #create new rental
            rentitem.is_available = False
            rentitem.save()
            rental = hmod.Rental()

            rental.name = rentitem
            rental.rental_date = datetime.date.today()
            rental.due_date = (datetime.date.today() + datetime.timedelta(days=30))
            rental.customer = request.user
            print(rental)
            rental.save()



        template_vars['rental_cart'] = rental_cart
        template_vars['current_cart'] = current_cart

        ###############################send email############################### code
        if request.user.email != "":
            subject = "CHF Receipt"
            to = [request.user.email]
            from_email = 'rodcox89@gmail.com'

            template_vars['total'] = get_total(request)
            template_vars['confirmation'] = resp

            message = templater.render(request, 'confirmationemail.html', template_vars)

            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()







        del request.session['rental_cart']
        del request.session['shopping_cart']

        return templater.render_to_response(request, 'confirmation.html', template_vars)

    template_vars = {


    }

    return templater.render_to_response(request, 'index.html', template_vars)

class CheckoutForm(forms.Form):
    First = forms.CharField(required=True,initial='Gov',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First'}))
    Last = forms.CharField(required=True,initial='Allen', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last'}))
    Address = forms.CharField(required=True,initial='783 yahoo st', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    City = forms.CharField(required=True,initial='Orem', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    State = forms.CharField(required=True,initial='Utah', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    Zip = forms.CharField(required=True, max_length=100,initial='84559', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip'}))
    Name = forms.CharField(required=True,initial='Cosmo Limesandal', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name on Card'}))
    CardNumber = forms.CharField(required=True,initial='4732817300654', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Number'}))
    ExpirationMonth = forms.CharField(required=True,initial='10', max_length=2,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM'}))
    ExpirationYear = forms.CharField(required=True,initial='15', max_length=2,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YY'}))
    Cvv = forms.CharField(required=True,initial='411', max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVV'}))
