# yusha144\urls.py
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),  # панель администратора на главной странице приложения main
                  path('', include('main.urls'))  # переходим в urls на главной странице приложения main
              ] + static(settings.STATIC_URL, document_roo=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
