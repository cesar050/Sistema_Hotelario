from django.urls import path
from . import views
from .views import base

urlpatterns = [
    path('',views.base, name='base'),
]
