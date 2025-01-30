from django.http import JsonResponse
from django.shortcuts import render
from apps.dashboard.models import UserTable
import json

def register_view(request):
    if request.method == 'POST':
        try:
            # Parse o JSON enviado pelo Fetch API
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            # Verificação básica de campos obrigatórios
            if not name or not email or not password:
                return JsonResponse({'error': "Todos os campos são obrigatórios."}, status=400)

            # Verificar se o email já está em uso
            if UserTable.objects.filter(email=email).exists():
                return JsonResponse({'error': "Este e-mail já está registrado."}, status=400)
            
            # Verificar se o username já está em uso
            if UserTable.objects.filter(name=name).exists():
                return JsonResponse({'error': "Este username já está registrado."}, status=400)

            # Criar o usuário
            UserTable.objects.create(name=name, email=email, password=password)
            return JsonResponse({'message': "Usuário registrado com sucesso!"}, status=201)
        except Exception as e:
            return JsonResponse({'error': f"Erro ao criar usuário: {str(e)}"}, status=500)

    # Para GET, renderize o template normalmente
    elif request.method == 'GET':
        return render(request, 'register/register.html')

    # Para outros métodos, retorne erro 405
    return JsonResponse({'error': "Método não permitido."}, status=405)
