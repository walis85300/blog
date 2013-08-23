# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime
from operator import itemgetter, attrgetter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from publicaciones.models import *

def index(request):

	posts_lista = Post.objects.all()
	paginator = Paginator(posts_lista,3)
	pagina = request.GET.get('page')

	try:
		posts = paginator.page(pagina)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_page)
	
	p = sorted(posts, key=attrgetter('id'),reverse=True)

	return render_to_response('index.html',{'posts':p},context_instance=RequestContext(request))

def post(request,id_post):
	dato = get_object_or_404(Post,pk=id_post)
	
	return render_to_response('posts.html',{'posts':dato},context_instance=RequestContext(request))


