import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MarketFilterForm, SellAccountForm
from .models import Product


def index(request):
    return render(request, 'market/index.html')


def market(request):
    form = MarketFilterForm()
    sell = SellAccountForm()
    if request.method == 'POST':
        data = request.POST
        links = [i.link for i in list(Product.objects.all())]
        link = dict(data)['link']
        if "".join(link) in links:
            messages.error(request, 'Этот аккаунт уже находится на продаже.')
        else:
            Product.objects.create(title=data['title'], price=data['price'], link=data['link'], phone=data['phone'],
                                   mail=data['mail'], last_activity=datetime.datetime.now())
            messages.success(request, 'Аккаунт успешно выставлен на маркет.')
    return render(request, 'market/market.html', {'form': form, 'sell': sell, 'items': list(Product.objects.all())})


def item(request):
    return render(request, 'market/item.html')


def sell_account(request):
    pass
