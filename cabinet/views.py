from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Subscription
from django.contrib.auth.decorators import login_required
from .forms import SettingsProfileForm
from .payment import create_bill, check_state


def profile(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    subscribed = False
    if Subscription.objects.filter(subscriber=request.user, subscribed_to=user):
        subscribed = True
    if request.method == 'POST':
        # Проверка на то - есть ли подписка этого пользователя на этого юзера.
        if not Subscription.objects.filter(subscriber=request.user, subscribed_to=user):
            Subscription.objects.create(subscriber=request.user, subscribed_to=user)
        else:
            subscribed = True
    return render(request, 'cabinet/userprofile.html', {'user': user, 'subscribed': subscribed})


@login_required
def settings_profile(request):
    bill = create_bill(100)
    form = SettingsProfileForm(request.POST, request.FILES)
    if check_state(bill['id']):
        user = get_object_or_404(UserProfile, pk=request.user.pk)
        print(user)
    else:
        print('no')

    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            for field_name, field_value in cleaned_data.items():
                if field_value:
                    setattr(request.user, field_name, field_value)
            UserProfile.save(request.user)
    return render(request, 'cabinet/settings.html', {'form': form, 'url_payment': bill['url']})
