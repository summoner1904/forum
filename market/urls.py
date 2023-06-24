from django.urls import path
from .views import index, market, item

app_name = 'market'

urlpatterns = [
    path('', index, name='index'),
    path('market/', market, name='market'),
    path('item/<int:pk>', item, name='item')
]
