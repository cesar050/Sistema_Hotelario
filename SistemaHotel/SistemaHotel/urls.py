"""
URL configuration for SistemaHotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1e8ee1d (inicio del modelado)
=======


urlpatterns = [
<<<<<<< HEAD
>>>>>>> 67d9ed0 (inicio del modelado)
=======
<<<<<<< HEAD
>>>>>>> f6d1e94 (ViewsTemplates)
=======


urlpatterns = [
>>>>>>> 1e8ee1d (inicio del modelado)
    path('', include('core.urls')),
        path('admin/', admin.site.urls),
        path('api/', include('core.urls')),

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
]
=======
=======
>>>>>>> 4c3a679 (sitemaHotel)
=======
]
=======
>>>>>>> f6d1e94 (ViewsTemplates)
=======
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
>>>>>>> 4c3a679 (sitemaHotel)
    path('', include('adminHotel.urls')),  # Esto es para la ruta raíz
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/', include('adminHotel.urls')),
    path('api/', include('user_manager.urls')),
    path('api/', include('client_manager.urls')),
    path('api/', include('hotel_manager.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('api/', include('reservation_manager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> b2277ad (ViewsTemplates)
=======
]
>>>>>>> 1e8ee1d (inicio del modelado)
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 4c3a679 (sitemaHotel)
=======
    path('api/', include('reservation_manager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> b2277ad (ViewsTemplates)
=======
]
>>>>>>> 67d9ed0 (inicio del modelado)
=======
    path('api/', include('reservation_manager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> b2277ad (ViewsTemplates)
>>>>>>> f6d1e94 (ViewsTemplates)
=======
]
>>>>>>> 1e8ee1d (inicio del modelado)
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 4c3a679 (sitemaHotel)
=======
    path('api/', include('reservation_manager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> b2277ad (ViewsTemplates)
