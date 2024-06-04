from django.urls import path
from . import views

urlpatterns = [
    path('another/', views.another_example_view, name='another_example_view'),
]
