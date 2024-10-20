from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


def file_path_html(arquivo):
    file_path = f"C:/Users/augus/Desktop/projeto_investimentos/invista_me/templates/investimentos/{arquivo}"
    return file_path


def pagina_contato(request):
    return HttpResponse("Para dúvidas, enviar um e-mail para contato@suporte.com")


def minha_historia(request):
    pessoa = {
        "nome": "Joao",
        "idade": 23,
        "hobby": "Games, Programar e assistir filmes/series",
        "data_nascimento": ["06/09/2000"],
        "local_natal": "Resende-RJ",
    }
    return render(
        request,
        file_path_html("minha_historia.html"),
        pessoa,
    )


def investimentos(request):
    dados = {"dados": Investimento.objects.all()}
    return render(request, file_path_html("investimentos.html"), context=dados)


def detalhe(request, id_investimento):
    dados = {"dados": Investimento.objects.get(pk=id_investimento)}
    return render(request, file_path_html("detalhe.html"), dados)


@login_required
def criar(request):
    if request.method == "POST":
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect("investimentos")
    else:
        investimento_form = InvestimentoForm()
        formulario = {"formulario": investimento_form}
        return render(
            request, file_path_html("novo_investimento.html"), context=formulario
        )


@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == "GET":
        formulario = InvestimentoForm(instance=investimento)
        formulario_dict = {"formulario": formulario}
        return render(
            request, file_path_html("novo_investimento.html"), formulario_dict
        )
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect("investimentos")


@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    investimento_check_id = {"item": investimento}
    if request.method == "POST":
        investimento.delete()
        return redirect("investimentos")
    return render(
        request, file_path_html("confirmar_exclusao.html"), investimento_check_id
    )
