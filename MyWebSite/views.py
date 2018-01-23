from django.shortcuts import render
from django.http import HttpResponse
from MyWebSite.models import tb_user


# Create your views here.
def index(request):
    context = {}
    context['fullname'] = 'abcd'
    context['email'] = 'edwin.nie@msc.com'
    return render(request, 'MyWebSite/index.html', context)
    # return HttpResponse("Hello world. You are at the MyWebSite index.")


def detail(request, Id):
    users = tb_user.objects.order_by('Id')
    list = []

    for u in users:
        list.append(u)
    return HttpResponse("You're looking at user %s." % users[0].Email)


def results(request, Id):
    response = "You're looking at the results of question %s."


    return HttpResponse(response % Id)


def vote(request, Id):
    return HttpResponse("You're voting on question %s." % Id)
