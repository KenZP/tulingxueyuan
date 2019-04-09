from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views function need a request
def do_normalmap(request):
    return HttpResponse("Hello Django")

#http://127.0.0.1:8000/withparam/2019/04
def withparam(request,year,month):
    return HttpResponse("this is with param {0},{1}".format(year,month))

def do_app(r):
	return HttpResponse("this is a son rout")

def do_param2(r,pn):
	return HttpResponse("page number is {0}".format(pn))

def extremParam(r,name):
	return HttpResponse("My name is {0}".format(name))