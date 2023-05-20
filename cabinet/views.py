from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required


def profile(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'cabinet/userprofile.html', {'user': user})


@login_required
def settings_profile(request):
    if request.method == 'POST':
        username = request.POST['username']


    return render(request, 'cabinet/settings.html')
