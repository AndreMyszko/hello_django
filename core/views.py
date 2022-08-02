from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from core.models import Evento
HttpRequest

# Create your views here.


def index(request):
    return redirect('/agenda/')


def user(request, firstname, lastname, age):
    return HttpResponse(
        '<h2>hello world</h2>'
        '<br> be wolcome'
        '<br> name: <b>{} {}</b>'
        '<br> age: <b>{}</b>'
        .format(firstname, lastname, age))


def lista_agendamentos(request):
    evento = Evento.objects.all()
    data = {'eventos': evento}
    return render(request, 'agenda.html', data)
