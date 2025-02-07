from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from apps.dashboard.models import UserTable
import json

class register_view(APIView):
    def GET(self, request):
        return render(request, 'register/register.html')

    def POST(self, request):
        try:
            # Parse o JSON enviado pelo Fetch API
            data = request.data
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            # Verificação básica de campos obrigatórios
            if not all(name, email, password):
                return Response({'error': "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

            # Verificar se o email já está em uso
            if UserTable.objects.filter(email=email).exists():
                return Response({'error': "Este e-mail já está registrado."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Verificar se o username já está em uso
            if UserTable.objects.filter(name=name).exists():
                return Response({'error': "Este username já está registrado."}, status=status.HTTP_400_BAD_REQUEST)

            # Criar o usuário
            UserTable.objects.create(name=name, email=email, password=make_password(password))
            return Response({'message': "Usuário registrado com sucesso!"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': f"Erro ao criar usuário: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)