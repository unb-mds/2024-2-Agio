import os

os.system("cd src && gunicorn mysite.wsgi")