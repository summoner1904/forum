from django.shortcuts import render
from .forms import MarketFilterForm


def index(request):
    return render(request, 'market/index.html')


def market(request):
    form = MarketFilterForm()
    return render(request, 'market/market.html', {'form': form})


def item(request):
    return render(request, 'market/item.html')

