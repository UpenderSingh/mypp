from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
def index(request):
	# context_instance = RequestContext(request)
	context = {}
	context['boldmessage'] = "I am bold font from the context"
	return render(request, 'index.html', locals())
