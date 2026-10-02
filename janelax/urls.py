from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('cadastro/sucesso/', views.boas_vindas, name='boas_vindas'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:usuario_id>/', views.detalhe_usuario, name='detalhe_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
]