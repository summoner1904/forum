from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Subscription, Posts
from django.contrib.auth.decorators import login_required
from .forms import SettingsProfileForm, PostProfileForm
from .payment import create_bill, check_state
from django.contrib import messages


def profile(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    post_form = PostProfileForm(request.POST)
    subscribed = False
    if post_form.is_valid():
        data = post_form.cleaned_data
        poster = UserProfile.objects.get(pk=pk)
        Posts.objects.create(sender=request.user, poster=poster, text_post=data['text_post'])
    posts = Posts.objects.filter(poster_id=pk)
    subscription = Subscription.objects.filter(subscriber_id=pk)

    if request.method == 'POST':
        # Проверка на то - есть ли подписка этого пользователя на этого юзера.
        if not Subscription.objects.filter(subscriber=request.user, subscribed_to=user):
            Subscription.objects.create(subscriber=request.user, subscribed_to=user)
            subscribed = True
            return render(request, 'cabinet/userprofile.html', {'user': user, 'subscribed': subscribed, 'post_form': post_form, 'posts': posts})
        else:
            sub = Subscription.objects.filter(subscriber=request.user, subscribed_to=user)
            sub.delete()
            subscribed = False
    return render(request, 'cabinet/userprofile.html', {'user': user, 'subscribed': subscribed, 'post_form': post_form, 'posts': posts, 'subscription': subscription})


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

