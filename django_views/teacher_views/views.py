from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
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


# http://127.0.0.1:8000/v8/?k1=1&v1=2
def v8_get(request):
    rst = ""
    for k, v in request.GET.items():
        rst += k + "-->" + v
        rst += ","

    return HttpResponse("Get value of request is {0}".format(rst))


def v9_get(request):
    return render_to_response("for_post.html")


def v9_post(request):
    rst = ""
    for k, v in request.POST.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("Get value of POST is {0}".format(rst))


def render_test(request):
    # c = dict()
    rsp = render(request, "render.html")
    return rsp


def render_test2(request):
    c = dict()
    c["name"] = "Ken"
    c["name1"] = "Ken1"
    c["name2"] = "Ken2"
    rsp = render(request, "render2.html", context=c)
    return rsp


def render_test3(request):
    from django.template import loader

    t = loader.get_template("render2.html")
    print (type(t))
    r = t.render({"name": "ken"})
    print (type(r))
    return HttpResponse(r)


def render_test4(request):
    rsp = render_to_response("render2.html", context={"name": "kenkenken"})
    return rsp


def get404(request):
    from django.views import defaults
    #return defaults.page_not_found(request,Exception)
    return defaults.page_not_found(request,template_name="render.html")
