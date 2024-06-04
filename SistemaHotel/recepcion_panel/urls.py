from django.urls import path
from . import views

urlpatterns = [
    path('some-route/', views.some_view, name='some-view'),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
]