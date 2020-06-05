from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include

from .views import UserViewSet
from . import views
from .apiview import CustomAuthToken

router = routers.DefaultRouter()
router.register(r'users',UserViewSet,r"users")


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Session Login
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^auth/$',  views.login_form, name='login_form'),
    # path('signin/',LoginView.as_view()),
    # path('register/',Registration.as_view()),
    url(r'^api-token-auth/', CustomAuthToken.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = 'accounts'