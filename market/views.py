import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MarketFilterForm, SellAccountForm
from .models import Product


def index(request):
    return render(request, 'market/index.html')


def market(request):
    form = MarketFilterForm(request.POST)
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
        if form.is_valid():
            data = form.cleaned_data
            title = data.get('title', '')
            min_price = data.get('min_price')
            max_price = data.get('max_price')

            products = Product.objects.all()

            if title:
                products = products.filter(title__icontains=title)

            if min_price is not None and max_price is not None:
                products = products.filter(price__range=(min_price, max_price))
            elif min_price is not None:
                products = products.filter(price__gte=min_price)
            elif max_price is not None:
                products = products.filter(price__lte=max_price)
            if not products:
                no_results_message = "Подходящих товаров не найдено."
                return render(request, 'market/market.html', {'no_results_message': no_results_message, 'form': form, 'sell': sell})

            return render(request, 'market/market.html', {'products': products, 'form': form, 'sell': sell})

    return render(request, 'market/market.html', {'form': form, 'sell': sell, 'items': items})


def item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'market/item.html', {'item': product})

