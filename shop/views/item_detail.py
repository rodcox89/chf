from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
import random
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import homepage.models as hmod

templater = get_renderer('shop')

@view_function
def process_request(request):



    template_vars = {
    }

    item = hmod.Item.objects.get(id = request.urlparams[0])

    template_vars['item'] = item
    




    return templater.render_to_response(request, 'item_detail.html', template_vars)
