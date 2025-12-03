from django.shortcuts import render, redirect
from .models import Receita
from .forms import ReceitaForm


def lista_receitas(request):
    receitas = Receita.objects.all().order_by('-criado_em')
    return render(request, 'receitas/lista_receitas.html', {'receitas': receitas})


def criar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_receitas')
    else:
        form = ReceitaForm()

    return render(request, 'receitas/criar_receita.html', {'form': form})
