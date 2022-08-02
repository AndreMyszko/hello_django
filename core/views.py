from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
HttpRequest

# Create your views here.


def about(request):
    return HttpResponse('<h1>Python with Django API</h1> SUCCESS<br>working properly')


def user(request, firstname, lastname, age):
    return HttpResponse(
        '<h2>hello world</h2>'
        '<br> be wolcome'
        '<br> name: <b>{} {}</b>'
        '<br> age: <b>{}</b>'
        .format(firstname, lastname, age))
