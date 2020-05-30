
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django_mongoengine import mongo_admin

urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('mongoadmin/', mongo_admin.site.urls),

]

#django built in server-static and media files
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
