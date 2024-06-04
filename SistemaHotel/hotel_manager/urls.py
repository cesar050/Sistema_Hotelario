from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f6d1e94 (ViewsTemplates)
    path('another/', views.another_example_view, name='another_example_view'),
=======
    path('habitaciones/', views.listar_habitaciones, name='habitaciones'),
>>>>>>> b2277ad (ViewsTemplates)
<<<<<<< HEAD
=======
    # Define tus patrones de URL aquí
    # Por ejemplo:
    # path('', views.index, name='index'),
>>>>>>> 4c3a679 (sitemaHotel)
=======
    path('habitaciones/', views.listar_habitaciones, name='habitaciones'),
>>>>>>> b2277ad (ViewsTemplates)
=======
>>>>>>> f6d1e94 (ViewsTemplates)
=======
    # Define tus patrones de URL aquí
    # Por ejemplo:
    # path('', views.index, name='index'),
>>>>>>> 4c3a679 (sitemaHotel)
=======
    path('habitaciones/', views.listar_habitaciones, name='habitaciones'),
>>>>>>> b2277ad (ViewsTemplates)
]
