from django.urls import path
from .views import profile, settings


app_name = 'profile'


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/settings', settings, name='settings'),
]