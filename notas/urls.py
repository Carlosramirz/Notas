from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('register/', views.register, name='register'),
    path('crear/', views.crear_nota, name='crear_nota'),
    path('editar/<int:nota_id>/', views.editar_nota, name='editar_nota'),
    path('eliminar/<int:nota_id>/', views.eliminar_nota, name='eliminar_nota')
]