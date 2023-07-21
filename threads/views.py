from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def create_thread(request):
    return render(request, 'threads/new_thread.html')
