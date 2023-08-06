from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('store.urls', namespace='store')),
    path('admin/', admin.site.urls),
]
