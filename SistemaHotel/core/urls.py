<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('agregar_persona_usuario/', views.agregar_persona_usuario, name='agregar_persona_usuario'),
    path('', index, name='index'),
]
=======
from django.urls import path
from . import views
from .views import index

urlpatterns = [
<<<<<<< HEAD
=======
from django.urls import path
from . import views
from .views import index

urlpatterns = [
<<<<<<< HEAD
>>>>>>> 1e8ee1d (inicio del modelado)
    path('some-route/', views.some_view, name='some-view'),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
<<<<<<< HEAD
]
>>>>>>> 1e8ee1d (inicio del modelado)
=======
    path('agregar_persona_usuario/', views.agregar_persona_usuario, name='agregar_persona_usuario'),
    path('', index, name='index'),
]
>>>>>>> 4c3a679 (sitemaHotel)
=======
]
>>>>>>> 1e8ee1d (inicio del modelado)
=======
    path('agregar_persona_usuario/', views.agregar_persona_usuario, name='agregar_persona_usuario'),
    path('', index, name='index'),
]
>>>>>>> 4c3a679 (sitemaHotel)
