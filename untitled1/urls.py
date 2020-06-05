'''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('myapp.urls')),

    path('admin/', admin.site.urls),


]

#django built in server-static and media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import ObtainAuthToken



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),

    ]
app_name = 'accounts'
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)