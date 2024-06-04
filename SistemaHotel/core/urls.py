from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('agregar_persona_usuario/', views.agregar_persona_usuario, name='agregar_persona_usuario'),
    path('', index, name='index'),
    path('', views.home, name='home'),
]
