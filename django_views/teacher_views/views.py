from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.


def teacher(r):
	return HttpResponse("this is a teacher views")

def v2_exception(r):
	raise Http404
	return HttpResponse("OK")

def v10_1(request):
    return HttpResponseRedirect("/v11")
           
def v10_2(request):
    return HttpResponseRedirect(reverse("v11"))
           
def v11(request):
    return HttpResponse("this is v11 return")  

#http://127.0.0.1:8000/v8/?k1=1&v1=2
def v8_get(request):
	rst = ""
	for k,v in request.GET.items():
		rst += k + "-->" + v
		rst += ","

	return HttpResponse("Get value of request is {0}".format(rst))

def v9_get(request):
	return render_to_response("for_post.html")

def v9_post(request):
	rst = ""
	for k,v in request.POST.items():
		rst += k + "-->" + v
		rst += ","
	return HttpResponse("Get value of POST is {0}".format(rst))