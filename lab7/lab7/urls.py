from django.contrib import admin
from django.urls import path, include
from destinos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('destinos/', include('destinos.urls')),
    path('', views.index, name='index'),
]
