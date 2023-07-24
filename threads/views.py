from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from cabinet.models import UserProfile
from .forms import NewThreadForm
from .models import Thread, Category

@login_required
def create_thread(request):
    form = NewThreadForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            thread_post = Thread.objects.create(user_id=request.user.pk, **data)
            request.user.messages += 1  # Обновление статистики в профиле
            UserProfile.save(request.user)
            return redirect(reverse('threads:thread', kwargs={'thread_id': thread_post.pk}))
    return render(request, 'threads/new_thread.html', {'form': form})


def thread(request, thread_id):
    thread_post = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'threads/thread.html', {'thread': thread_post})


def category_threads(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    threads = Thread.objects.filter(category=category)
    return render(request, 'threads/category_thread.html', {'threads': threads})
