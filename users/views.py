from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def file_path_html(arquivo):
    file_path = f"C:/Users/augus/Desktop/projeto_investimentos/usuarios/templates/usuarios{arquivo}"
    return file_path


def novo_usuario(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get("username")
            messages.success(request, f"O usuário {usuario} foi criado com sucesso!")
            return redirect("login")
    else:
        formulario = UserRegisterForm()

    return render(request, file_path_html("registrar.html"), {"formulario": formulario})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
