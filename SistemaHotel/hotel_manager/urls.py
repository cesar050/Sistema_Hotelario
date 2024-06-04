from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('another/', views.another_example_view, name='another_example_view'),
=======
    path('habitaciones/', views.listar_habitaciones, name='habitaciones'),
>>>>>>> b2277ad (ViewsTemplates)
]
