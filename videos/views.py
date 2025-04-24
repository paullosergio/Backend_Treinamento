# videos/views.py
from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class VideoUploadView(APIView):
    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Vídeo enviado com sucesso!"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoListView(generics.ListAPIView):
    """
    Lista todos os vídeos.
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer


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
