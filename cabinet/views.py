from django.shortcuts import render


def profile(request):
    return render(request, 'cabinet/profile.html')


def settings(request):
    return render(request, 'cabinet/settings.html')
