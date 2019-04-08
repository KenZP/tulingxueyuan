from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views function need a request
def do_normalmap(request):
    return HttpResponse("Hello Django")