from django.shortcuts import render
from cabinet.models import UserProfile
from .models import Thread
from .forms import NewThreadForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def create_thread(request):
    form = NewThreadForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            Thread.objects.create(user_id=request.user.pk, **data)
            form = NewThreadForm()
            request.user.messages += 1
            UserProfile.save(request.user)
    return render(request, 'threads/new_thread.html', {'form': form})
