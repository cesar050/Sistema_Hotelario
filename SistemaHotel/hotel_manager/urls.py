from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path('another/', views.another_example_view, name='another_example_view'),
=======
    path('habitaciones/', views.listar_habitaciones, name='habitaciones'),
>>>>>>> b2277ad (ViewsTemplates)
=======
    path('habitaciones/', views.listar_habitaciones, name='habitaciones'),
>>>>>>> b2277ada42f3b63703deac7e599c1eeae3e34251
]
