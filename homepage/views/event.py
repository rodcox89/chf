from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
import random
from django import forms
import homepage.models as hmod

templater = get_renderer('homepage')

@view_function
def process_request(request):

    #empty params
    params = {}
    eventid = request.urlparams[0]

    #get all events
    events = hmod.Event.objects.get(id=eventid)

    #get items for sale
    items = hmod.Item.objects.all()

    params['event'] = events
    params['items'] = items
    return templater.render_to_response(request, 'event.html', params)
