from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Video
from .serializers import VideoSerializer


class VideoUploadView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Vídeo enviado com sucesso!"},
            status=status.HTTP_201_CREATED,
        )

class VideoListView(generics.ListAPIView):
    """
    Lista todos os vídeos.
    """

class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class VideoByBankListView(generics.ListAPIView):
    """
    Lista vídeos filtrados por banco.
    """

    serializer_class = VideoSerializer

    def get_queryset(self):
        bank = self.request.query_params.get("bank", None)
        if bank:
            return Video.objects.filter(bank=bank)
        return Video.objects.all()
