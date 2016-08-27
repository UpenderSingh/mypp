from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def hompage(request):
	return HttpResponse("hello")
