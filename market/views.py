import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MarketFilterForm, SellAccountForm
from .models import Product


def index(request):
    return render(request, 'market/index.html')


def market(request):
    form = MarketFilterForm()
    sell = SellAccountForm(request.POST)
    items = list(Product.objects.all())
    if request.method == 'POST':
        if sell.is_valid():
            data = sell.cleaned_data
            lst = list(Product.objects.all())
            if data['link'] in [i.link for i in lst]:
                messages.error(request, 'Этот аккаунт уже есть на маркете.')
                return render(request, 'market/market.html', {'form': form, 'sell': sell, 'items': items})
            Product.objects.create(**data)
            messages.success(request, 'Аккаунт успешно выставлен на маркет.')
    return render(request, 'market/market.html', {'form': form, 'sell': sell, 'items': items})


def item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'market/item.html', {'item': product})
