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

    template_vars = {}
    # today = datetime.date.today()
    #
    # start_date = datetime.date(today.year-20, today.month, today.day)
    # end_date = datetime.date(today.year, today.month, today.day-1)

    # overdueitems = hmod.Rental.objects.filter(due_date__range = (start_date, end_date))
    overdue_items = hmod.Rental.objects.filter(was_returned=False)

    ninety = datetime.date.today()-datetime.timedelta(days=90)
    sixty = datetime.date.today()-datetime.timedelta(days=60)
    thirty = datetime.date.today()-datetime.timedelta(days=30)


    print(overdue_items)
    thirties = []
    sixties = []
    nineties = []
    under = []

    for item in overdue_items:
        print('in for loop')
        if item.due_date < ninety:
            print('###############################more than 90############################### code')
            print(item.due_date)
            nineties.append(item)

        elif item.due_date < sixty:
            print('###############################more than 60############################### code')
            print(item.due_date)
            sixties.append(item)

        elif item.due_date < thirty:
            print('###############################more than 30############################### code')
            print(item.due_date)
            thirties.append(item)

        else:
            print('###############################it was less than 30############################### code')
            print(item.due_date)
            under.append(item)



    template_vars['thirties'] = thirties
    template_vars['sixties'] = sixties
    template_vars['nineties'] = nineties
    template_vars['under'] = under



    ninety = datetime.date.today()-datetime.timedelta(days=90)
    sixty = datetime.date.today()-datetime.timedelta(days=60)
    thirty = datetime.date.today()-datetime.timedelta(days=60)
    #  = hmod.Rental.objects.filter(due_date__range = (start_date, end_date))


    start_date = datetime.date.today()-datetime.timedelta(days=90)
    end_date = datetime.date.today()-datetime.timedelta(days=70)
    over_30 = hmod.Rental.objects.filter(due_date__range = (start_date, end_date))

    print(over_30)
    # params['over_30'] = over_30
    # print(params['over_30'])



    return templater.render_to_response(request, 'overdue.html', template_vars)

################################
## Edit a user
