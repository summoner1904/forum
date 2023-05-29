from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import SettingsProfileForm


def profile(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'cabinet/userprofile.html', {'user': user})


@login_required
def settings_profile(request):
    form = SettingsProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            for field_name, field_value in cleaned_data.items():
                if field_value:
                    setattr(request.user, field_name, field_value)
            UserProfile.save(request.user)
    return render(request, 'cabinet/settings.html', {'form': form})
