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

  template_vars = {
  }










  return templater.render_to_response(request, 'account.html', template_vars)

@view_function
def edit(request):
  params = {}

  user = hmod.SiteUser.objects.get(id=request.user.id)


  form = UserEditForm(initial={
      'username': user.username,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'email': user.email,
  })

  if request.method == 'POST':
      form = UserEditForm(request.POST)
      form.userid = user.id
      if form.is_valid():
        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        return HttpResponse('''
        <script>
        window.location.href = window.location.href;
        </script>

        ''')


  params['form'] = form

  #user = hmod.SiteUser.objects.get(id=???)

  return templater.render_to_response(request, 'account.edit.html', params)

class UserEditForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    def clean_username(self):
        user_count = hmod.SiteUser.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Username already exists.")
        return self.cleaned_data['username']



@view_function
def changepassword(request):
  params = {}

  user = hmod.SiteUser.objects.get(id=request.user.id)


  form = PasswordChangeForm(user)

  print(form)
  if request.method == 'POST':
      print("It was a post")
      form = PasswordChangeForm(user,data=request.POST)
      print("It was a post")
      if form.is_valid():
          form.save()
          update_session_auth_hash(request, form.user)
          print("password changed")
          return HttpResponse('''
        <script>
        window.location.href = window.location.href;
        </script>

        ''')



  params['form'] = form

  #user = hmod.SiteUser.objects.get(id=???)

  return templater.render_to_response(request, 'account.changepassword.html', params)

class SetPasswordForm(forms.Form):


    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    print('password mismatch'),
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user


class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': ("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=("Old password"),
                                   widget=forms.PasswordInput)

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            print('wrong password'),
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',

            )
        return old_password

PasswordChangeForm.base_fields = OrderedDict(
    (k, PasswordChangeForm.base_fields[k])
    for k in ['old_password', 'new_password1', 'new_password2']
)
