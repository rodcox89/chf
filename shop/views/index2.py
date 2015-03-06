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

  template_vars = {
  }

  items = hmod.Item.objects.all()

  template_vars['items'] = items

  # item_id = request.urlparams[0]
  # item = hmod.Item()








  return templater.render_to_response(request, 'index2.html', template_vars)
