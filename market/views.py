import requests
from requests.exceptions import MissingSchema, ConnectionError
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from threads.models import Thread
from cabinet.payment import check_state
from .forms import MarketFilterForm, SellAccountForm
from .models import Product
from cabinet.models import UserProfile, Bill


def index(request):
    threads = Thread.objects.all()
    return render(request, 'market/index.html', {'threads': threads})


def market(request):
    bill = Bill.objects.filter(user=request.user)
    for i in bill:
        if check_state(i.bill_id):
            request.user.access = True
            UserProfile.save(request.user)
    form = MarketFilterForm(request.POST)
    sell = SellAccountForm(request.POST)
    items = list(Product.objects.all())
    if request.user.access == False:
        messages.error(request, 'У Вас нет доступа к маркету. Его можно приобрести в настройках профиля.')
        return render(request, 'market/market.html', {'form': form, 'sell': sell, 'items': items})
    else:
        messages.success(request, 'Ограничений нет.')
    if request.method == 'POST':
        if sell.is_valid():
            data = sell.cleaned_data
            lst = list(Product.objects.all())
            # Проверка на корректность URL адреса
            try:
                r = requests.get(url=data['link'])
            except (ConnectionError, MissingSchema):
                messages.error(request, 'Некорректная ссылка на аккаунт.')
                return render(request, 'market/market.html', {'form': form, 'sell': sell, 'items': items})
            if data['link'] in [i.link for i in lst]:
                messages.error(request, 'Этот аккаунт уже есть на маркете.')
                return render(request, 'market/market.html', {'form': form, 'sell': sell, 'items': items})
            Product.objects.create(**data)
            messages.success(request, 'Аккаунт успешно выставлен на маркет.')
            user = list(UserProfile.objects.filter(pk=request.user.pk))
            user[0].product += 1
            UserProfile.save(user[0])
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

