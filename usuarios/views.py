from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


class UserRegistrationView(APIView):
    """
    View para registro de usuários.
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "Usuário criado com sucesso",
                    "user": {
                        "id": user.id,
                        "cpf": user.username,
                        "email": user.email,
                        "name": user.first_name,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    View para autenticação de usuários.
    """
    def post(self, request):
        cpf = request.data.get('cpf')
        password = request.data.get('password')
        
        if not cpf or not password:
            return Response(
                {'error': 'CPF e senha são obrigatórios'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        user = authenticate(username=cpf, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'cpf': user.username,
                    'email': user.email,
                    'name': user.first_name,
                }
            })
            
        return Response(
            {'error': 'Credenciais inválidas'},
            status=status.HTTP_401_UNAUTHORIZED
        )

class CurrentUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)