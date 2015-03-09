from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from django.contrib.auth import login
from homepage import models as hmod
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from homepage.models import SiteUser
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')

@view_function
def process_request(request):

    params = {}

    user = hmod.SiteUser()
    print(user)

    form = SignupForm()

    print(form)
    if request.method == 'POST':
        print("It was a post")
        form = SignupForm(data=request.POST)
        print("It was a post")
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']

            user.save()
            print(user)
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, user)
            print("user created")
            return HttpResponseRedirect('/homepage/')



    params['form'] = form

    #user = hmod.SiteUser.objects.get(id=???)

    return templater.render_to_response(request, 'signup.html', params)


class SignupForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput)
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    def clean_username(self):
        user = hmod.SiteUser.objects.filter(username=self.cleaned_data['username'])
        if user.count() > 0:
            raise forms.ValidationError("Username already exists.")
        return self.cleaned_data['username']

################################
## Edit a user
