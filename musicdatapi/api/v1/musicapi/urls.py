# from django.conf.urls import urls
from django.conf.urls import url, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'music', views.MusicView)


urlpatterns = [
    url(r'^', include(router.urls)),
]

