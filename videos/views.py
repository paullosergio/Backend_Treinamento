from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer


class VideoUploadView(generics.CreateAPIView):
    """
    Permite o envio (upload) de um novo vídeo.

    Apenas usuários autenticados podem acessar este endpoint.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Cria um novo vídeo com base nos dados enviados no corpo da requisição.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Vídeo enviado com sucesso!"},
            status=status.HTTP_201_CREATED,
        )


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou remove um vídeo específico pelo ID.

    Apenas usuários autenticados podem acessar este endpoint.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]


class VideoByBankListView(generics.ListAPIView):
    """
    Lista vídeos com suporte a filtro por banco.

    Se o parâmetro de query `bank` for fornecido (ex: `/videos/?bank=BancoX`),
    os vídeos serão filtrados pelo nome do banco.

    Caso contrário, todos os vídeos serão retornados.
    """
    serializer_class = VideoSerializer

    def get_queryset(self):
        """
        Retorna a lista de vídeos, filtrando por banco se o parâmetro `bank` estiver presente.
        """
        bank = self.request.query_params.get("bank", None)
        if bank:
            return Video.objects.filter(bank=bank)
        return Video.objects.all()
