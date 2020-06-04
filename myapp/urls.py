'''
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myapp/form', views.model_form_upload, name='model_form_upload'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    '''
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views, apiviews

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^api/create_user/$', apiviews.UserCreate.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', apiviews.UserDetail.as_view()),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)