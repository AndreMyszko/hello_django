from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Evento

# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'usuário ou senha inválidos')
    return redirect('/')


@login_required(login_url='/login/')
def lista_agendamentos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    data = {'eventos': evento}
    return render(request, 'agenda.html', data)
