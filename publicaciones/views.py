# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime

def index(request):
	fecha = datetime.now()
	return render_to_response('index.html',{'fecha':fecha},context_instance=RequestContext(request))

