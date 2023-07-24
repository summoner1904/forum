from django.urls import path
from .views import create_thread, thread, category_threads

app_name = 'threads'


urlpatterns = [
    path('create_thread/', create_thread, name='new_thread'),
    path('thread/<int:thread_id>', thread, name='thread'),
    path('category/<int:category_id>', category_threads, name='category')
]