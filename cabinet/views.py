from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Subscription, Posts
from django.contrib.auth.decorators import login_required
from .forms import SettingsProfileForm, PostProfileForm
from .payment import create_bill, check_state
from django.contrib import messages


def profile(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    form = PostProfileForm(request.POST)
    posts = Posts.objects.filter(poster_id=pk).order_by('-pk')
    subscribes = Subscription.objects.filter(subscriber_id=pk)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            Posts.objects.create(sender=request.user, poster=user, text_post=data['text_post'])
            form = PostProfileForm()
        elif Subscription.objects.filter(subscriber=request.user, subscribed_to=user):
            sub = Subscription.objects.filter(subscriber=request.user, subscribed_to=user)
            sub.delete()
        else:
            Subscription.objects.create(subscriber=request.user, subscribed_to=user)
    subscribe = Subscription.objects.filter(subscriber=request.user, subscribed_to=user)
    return render(request, 'cabinet/profile.html', {'user': user, 'form': form, 'posts': posts,
                                                    'subscribes': subscribes, 'subscribe': subscribe})


@login_required
def settings_profile(request):
    bill = create_bill(100)
    form = SettingsProfileForm(request.POST, request.FILES)
    if check_state(bill['id']):
        user = get_object_or_404(UserProfile, pk=request.user.pk)
    else:
        pass
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            for field_name, field_value in cleaned_data.items():
                if field_value:
                    setattr(request.user, field_name, field_value)
            UserProfile.save(request.user)
            messages.success(request, 'Данные профиля успешно обновлены.')
        else:
            messages.error(request, 'Произошла ошибка при обновлении даных профиля.')
    return render(request, 'cabinet/settings.html', {'form': form, 'url_payment': bill['url']})

