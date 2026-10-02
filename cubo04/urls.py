"""
URL configuration for cubo04 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import include, path

from janelax import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('', include('janelax.urls')),
]
