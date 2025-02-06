"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import sys
print("PYTHON PATH:", sys.path)

try:
    import django
    print("Django está instalado. Versão:", django.__version__)
except ImportError:
    print("ERRO: Django NÃO está instalado!")

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

app = application