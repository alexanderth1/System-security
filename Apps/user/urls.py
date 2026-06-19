from django.urls import path
from Apps.user import views

urlpatterns = [
    path('', views.vista_login, name='login'),
    path('registro/', views.usuario_crear, name='usuario_crear'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil/editar/', views.usuario_editar, name='usuario_editar'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('supervisor/nuevo/', views.registrar_supervisor, name='registrar_supervisor'),
]