from django.urls import path
from .views import profile, settings_profile
from django.conf.urls.static import static
from django.conf import settings


app_name = "profile"


urlpatterns = [
    path("profile/<int:pk>", profile, name="profile"),
    path("settings", settings_profile, name="settings"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
