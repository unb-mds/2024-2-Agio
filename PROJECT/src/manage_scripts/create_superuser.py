import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.contrib.auth.models import User

# Dados do superusuário
USERNAME = "admin"
EMAIL = "admin@example.com"
PASSWORD = "admin123"

# Criar superusuário se não existir
if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superusuário criado com sucesso!")
else:
    print("Superusuário já existe.")
