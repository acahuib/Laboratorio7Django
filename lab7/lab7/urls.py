from django.contrib import admin
from django.urls import path, include
from destinos import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('destinos/', include('destinos.urls')),
    path('', views.inicio, name='inicio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
