from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

# Registro
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("lista_usuarios")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

# Login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("lista_usuarios")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# Logout
def user_logout(request):
    logout(request)
    return redirect("login")

# Lista de usuarios
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, "accounts/lista_usuarios.html", {"usuarios": usuarios})
