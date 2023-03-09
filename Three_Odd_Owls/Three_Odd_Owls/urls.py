from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('band.urls')),
    path('ourblog/', include('ourblog.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
