from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('ipaBLOG.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about_me/', include('ipaBLOG.urls')),
]