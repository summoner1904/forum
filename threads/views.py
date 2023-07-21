from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewThreadForm


@login_required
def create_thread(request):
    form = NewThreadForm()
    return render(request, 'threads/new_thread.html', {'form': form})
