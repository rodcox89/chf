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

    #get all events
    events = hmod.Event.objects.all()

    #month and day lists
    month = []
    day = []

    #for loop to get month and day
    for event in events:
        newmonth = event.start_date.strftime('%b')
        newday = event.start_date.strftime('%d')
        month.append(newmonth)
        day.append(newday)

    #pass event, month and day to festivals.html
    params['months'] = month
    params['days'] = day
    params['events'] = events
    return templater.render_to_response(request, 'festivals.html', params)
