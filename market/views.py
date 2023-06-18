import datetime

from django.shortcuts import render, redirect
from .forms import MarketFilterForm, SellAccountForm
from .models import Product


def index(request):
    return render(request, 'market/index.html')


def market(request):
    form = MarketFilterForm()
    sell = SellAccountForm()
    items = list(Product.objects.all())
    print(items)
    if request.method == 'POST':
        if not request.user.access:
            return redirect("cabinet:profile", request.user.pk)
        data = request.POST
        Product.objects.create(title=data['title'], price=data['price'], link=data['link'], phone=data['phone'],
                               mail=data['mail'], last_activity=datetime.datetime.now())
    return render(request, 'market/market.html', {'form': form, 'sell': sell, 'items': items})


def item(request):
    return render(request, 'market/item.html')


def sell_account(request):
    pass

