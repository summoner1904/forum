from django.shortcuts import render


def index(request):
    return render(request, 'market/index.html')


def market(request):
    return render(request, 'market/market.html')


def item(request):
    return render(request, 'market/item.html')

