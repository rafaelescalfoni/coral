from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *


def index(request):
    return render(request, "index.html", {})

def login(request):
    general_error = ""

    if request.POST:
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                general_error = f"Você já está logado(a) como {username}"
                return redirect("/home")
            else:
                general_error = "Usuário ou senha inválidos"
        else:
            general_error = "Usuário ou senha inválidos"

    form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form, "general_error": general_error})

def logout(request):
    auth_logout(request)
    return redirect("/")

@login_required
def home(request):
    current_user = request.user
    return render(request, "home.html", {"current_user": current_user})

@login_required
def project(request, id):
    current_user = request.user
    return render(request, "project.html", {"current_user": current_user, "id": id})

@login_required
def graph_specialist(request, proj_id):
    current_user = request.user
    return render(request, "graph_specialist.html", {"current_user": current_user})

@login_required
def graph_reputation(request, proj_id):
    current_user = request.user
    return render(request, "graph_reputation.html", {"current_user": current_user})

@login_required
def graph_reputation_filter(request, proj_id):
    current_user = request.user
    return render(request, "graph_reputation_filter.html", {"current_user": current_user})

@login_required
def ecosystem_graph(request):
    current_user = request.user
    return render(request, "ecosystem_graph.html", {"current_user": current_user})

@login_required
def details(request, proj_id, page):
    current_user = request.user
    return render(request, "details.html", {"current_user": current_user, "page": page})