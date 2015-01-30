from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
import random

templater = get_renderer('homepage')

@view_function
def process_request(request):
  params = {}
#  	 https://www.youtube.com/watch?v=z3SGIjIkV4E 12:59
  users = hmod.SiteUser.objects.all()
  params['events'] = users # 44:06
 
  return templater.render_to_response(request, 'events.html', params)



  