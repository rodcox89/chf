from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from django.contrib.auth import login
from homepage import models
from homepage.models import SiteUser
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('administration')

@view_function
def process_request(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            django.contrib.auth.login(request, form.user)
            return HttpResponseRedirect('/administration/users/')


    template_vars = {
        'form': form,
	}

    return templater.render_to_response(request, 'login.html', template_vars)


class LoginForm(forms.Form):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

	# These below functions are used to display error messages for incorrect
	# user name and password. Notice clean_(name) must match the field name.

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		self.user = django.contrib.auth.authenticate(username=username, password=password)
		print(self.user)
		if self.user == None:
			raise forms.ValidationError('Incorrect username/password.')

		return self.cleaned_data

################################
## Edit a user
