from django.shortcuts import render
from django.db.models import Sum
from .models import Movimentacao

def dashboard(request):
    # Total de receitas
    total_receitas = Movimentacao.objects.filter(
        tipo=Movimentacao.Tipo.RECEITAS
    ).aggregate(Sum('valor'))['valor__sum'] or 0

    # Total de despesas
    total_despesas = Movimentacao.objects.filter(
        tipo=Movimentacao.Tipo.DESPESAS
    ).aggregate(Sum('valor'))['valor__sum'] or 0

    # Saldo
    saldo = total_receitas - total_despesas

    # Últimos 10 movimentos
    movimentos = Movimentacao.objects.order_by('-data')[:10]

    context = {
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
        'movimentos': movimentos,
    }

    return render(request, 'dashboard.html', context)