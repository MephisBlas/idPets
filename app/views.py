from sqlite3 import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    return render (request, 'paginas/inicio.html')
def nosotros(request):
    return render (request,'paginas/nosotros.html')

def Mascotas(request):
    return render(request, 'Mascotas/index.html')

def registrar_mascotas(request):
    return render(request, 'Mascotas/registrar_mascotas.html')

def editar_mascotas(request):
    return render(request, 'Mascotas/editar_mascotas.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'paginas/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
def login(request):
    return render (request,'paginas/login.html')

