# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime
from publicaciones.models import *

def index(request):
	posts = Post.objects.all()
	return render_to_response('index.html',{'posts':posts},context_instance=RequestContext(request))

