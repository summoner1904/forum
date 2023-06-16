import datetime

from django.shortcuts import render
from .forms import MarketFilterForm, SellAccountForm
from .models import Product


def index(request):
    return render(request, 'market/index.html')


def market(request):
    form = MarketFilterForm()
    sell = SellAccountForm()
    if request.method == 'POST':
        data = request.POST
        Product.objects.create(title=data['title'], price=data['price'], link=data['link'], phone=data['phone'], mail=data['mail'], last_activity=datetime.datetime.now())
    return render(request, 'market/market.html', {'form': form, 'sell': sell})


def item(request):
    return render(request, 'market/item.html')


def sell_account(request):
    pass

