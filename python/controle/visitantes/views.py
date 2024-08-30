from django.shortcuts import render, redirect
from visitantes.forms import VisitanteForm
from porteiros.models import Porteiro
from django.contrib import messages

def registrar_visitante(request):
    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit = False)
            visitante.registrado_por = Porteiro.objects.get(id=1)
<<<<<<< HEAD
            
            visitante.save()
            
            messages.success(
                request,
                "O Visitante foi registrado com sucesso!"
            )
            
            
=======

            visitante.save()

            messages.success(
                request,
                "O visitante foi registrado com sucesso!"
            )
            
>>>>>>> a28a4823e10ba0c763df51bf9e7cd77d62e43dc4
            return redirect("index")

    context = {
        "nome_pagina": "Registrar visitante",
        "form": form,
    }

    return render(request, "registrar_visitante.html", context)