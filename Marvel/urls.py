"""Marvel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Marvels_Studio.urls')) # подключаем URL нашего приложения
]

# Джанго будет раздавть медия при включенном DEBUG

if settings.DEBUG: # если наш DEBUG включен, то
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # таким образом Django будет раздавать файлы при включенном Debug режиме