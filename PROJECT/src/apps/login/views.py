from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
import json
from apps.dashboard.models import UserTable
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie  # Corrigido: Agora o decorador está aplicado corretamente
class login_view(APIView):
    def GET(self, request):
        return render(request, 'login/login.html')

    def POST(self, request):
        try:
            data = request.data
            username = data.get('username')
            password = data.get('password')

            if not all(username, password):
                return Response({'error': "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

            # Buscar usuário pelo nome
            user = UserTable.objects.filter(name=username).first()
            if user is None or not check_password(password, user.password):
                return Response({'error': "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

            # Armazena o usuário na sessão
            request.session['user_id'] = user.id
            request.session['username'] = user.name

            return Response({'message': "Login realizado com sucesso!", 'redirect_url': "/dashboard/"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f"Erro ao realizar login: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)