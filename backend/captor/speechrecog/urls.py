from django.urls import path
from . import views


urlpatterns = [
    path("audio/", views.get_audio_subtitles.as_view())
    ]
