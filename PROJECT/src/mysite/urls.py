"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.homepage.views import (
    home_page_view,
)
from apps.dashboard.views import (
    dashboard_view,
)
from apps.login.views import (
    login_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='homepage'),
    path('/', home_page_view, name='homepage'),
    path('homepage/', home_page_view, name= "homepage"),
    path('dashboard/', dashboard_view, name= "dashboard"),
    path('login/', login_view.as_view(), name='login'),
    #path('register/', register_view, name='register'),
]
