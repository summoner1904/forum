from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import NewThreadForm
from .models import Thread

@login_required
def create_thread(request):
    form = NewThreadForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            thread_post = Thread.objects.create(user_id=request.user.pk, **data)
            return redirect(reverse('threads:thread', kwargs={'thread_id': thread_post.pk}))
    return render(request, 'threads/new_thread.html', {'form': form})


def thread(request, thread_id):
    thread_post = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'threads/thread.html', {'thread': thread_post})
