# videos/urls.py
from django.urls import path
from .views import VideoUploadView, VideoListView, VideoByBankListView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),  # Rota para upload de vídeo
    path('list/', VideoListView.as_view(), name='video-list'),  # Rota para listar todos os vídeos
    path('', VideoByBankListView.as_view(), name='video-filter-by-bank'),  # Rota para listar vídeos por banco
]
