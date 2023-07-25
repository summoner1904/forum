from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from cabinet.models import UserProfile
from .forms import NewThreadForm, NewCommentForm
from .models import Thread, Category, Comment


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
    form = NewCommentForm(request.POST)
    comments = Comment.objects.filter(thread_id=thread_id)
    if request.method == 'POST':
        if form.is_valid():
            request.user.messages += 1
            UserProfile.save(request.user)
            Comment.objects.create(sender=request.user, thread=thread_post, comment=form.cleaned_data['comment'])
            form = NewCommentForm()
    thread_post.views += 1  # Изменение просмотров на посте
    Thread.save(thread_post)
    return render(request, 'threads/thread.html', {'thread': thread_post, 'form': form, 'comments': comments})


def category_threads(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    threads = Thread.objects.filter(category=category)
    return render(request, 'threads/category_thread.html', {'threads': threads})
