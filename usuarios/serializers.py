from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(source='username')
    name = serializers.CharField(source='first_name')

    class Meta:
        model = User
        fields = ["id", "cpf", "email", "name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Como usamos "source", temos que acessar os campos aninhados
        try:
            user = User.objects.create_user(**validated_data)
            return user
        except IntegrityError as e:
            raise serializers.ValidationError({"detail": "Erro de integridade: o CPF já está registrado."})
        except Exception as e:
            raise serializers.ValidationError({"detail": str(e)})
