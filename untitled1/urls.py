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
from myapp.views import DataView
from rest_framework_mongoengine import routers

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'form', DataView, r"form")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)