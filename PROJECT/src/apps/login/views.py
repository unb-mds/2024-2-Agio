from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
import json
from apps.dashboard.models import UserTable
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie  # Corrigido: Agora o decorador está aplicado corretamente
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'error': "Todos os campos são obrigatórios."}, status=400)

            # Buscar usuário pelo nome
            user = UserTable.objects.filter(name=username).first()
            if user is None or not check_password(password, user.password):
                return JsonResponse({'error': "Credenciais inválidas."}, status=401)

            # Armazena o usuário na sessão
            request.session['user_id'] = user.id
            request.session['username'] = user.name

            return JsonResponse({'message': "Login realizado com sucesso!", 'redirect_url': "/dashboard/"}, status=200)

        except Exception as e:
            return JsonResponse({'error': f"Erro ao realizar login: {str(e)}"}, status=500)

    elif request.method == 'GET':
        return render(request, 'login/login.html')

    return JsonResponse({'error': "Método não permitido."}, status=405)

def logout_view(request):
    if request.method == 'POST':  # Logout via requisição AJAX
        try:
            request.session.flush()  # Remove todos os dados da sessão
            return JsonResponse({'message': "Logout realizado com sucesso!", 'redirect_url': "/login/"}, status=200)
        except Exception as e:
            return JsonResponse({'error': f"Erro ao realizar logout: {str(e)}"}, status=500)

    elif request.method == 'GET':  # Logout via navegação normal
        request.session.flush()
        return redirect('/login/')  # Redireciona para a página de login

    return JsonResponse({'error': "Método não permitido."}, status=405)
