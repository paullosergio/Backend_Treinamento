from django.urls import path
from .views import VideoUploadView, VideoListView, VideoByBankListView, VideoDetailView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    path('<int:id>/', VideoDetailView.as_view(), name='video-detail'),
    path('list/', VideoListView.as_view(), name='video-list'),
    path('', VideoByBankListView.as_view(), name='video-filter-by-bank'),
]
