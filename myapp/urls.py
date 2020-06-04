"""
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
"""
from django.conf.urls import url
from django.conf import settings

from django.urls import path, include

from . import views
from .apiviews import LoginView,Registration
from .serializers import Register

urlpatterns = [
    path('', views.home, name='home'),
    path('myapp/form', views.model_form_upload, name='model_form_upload'),
    path('data/',views.DataView.as_view(), name='data'),
    path('signin/',LoginView.as_view()),
    path('register/',Registration.as_view()),
]
