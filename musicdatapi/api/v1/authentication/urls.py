# from django.conf.urls import urls
from django.conf.urls import url, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'login', views.AuthenticationView)


urlpatterns = [
    # url(r'^', include(router.urls)),

    url(r'users', include('django.conf.auth.urls'))
]

