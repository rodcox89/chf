from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from bootstrap3_datetime.widgets import DateTimePicker
import homepage.models as hmod
import random
import datetime
templater = get_renderer('administration')

@view_function
# @permission_required('admin.delete_logentry', login_url='/administration/login/')
def process_request(request):
    params = {}

    today = datetime.date.today()

    start_date = datetime.date(today.year-20, today.month, today.day)
    end_date = datetime.date(today.year, today.month, today.day-1)

    overdueitems = hmod.Rentals.objects.filter(due_date__range = (start_date, end_date))

    params['items'] = overdueitems
    return templater.render_to_response(request, 'overdue.html', params)

################################
## Edit a user
