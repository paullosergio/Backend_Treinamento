from django.urls import path
from .views import VideoUploadView, VideoListView, VideoByBankListView, VideoDetailView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    path('', VideoByBankListView.as_view(), name='video-filter-by-bank'),
    path('<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
]
