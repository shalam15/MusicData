"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.contrib.auth import views as auth_views

from api.v1.account.views import UserViewSet
from api.v1.musicapi.views import MusicView
from api.v1.authentication.views import AuthenticationView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'music', MusicView)
router.register(r'auth',  AuthenticationView)

urlpatterns = [
    # DEFAULT HOMEPAGE
    url(r'^', include_docs_urls(title='API')),

    #ADMIN URL ENDPOINT
    url(r'^admin/', admin.site.urls),

    #API URL ENDPOINT
    # url(r'^api/', include(router.urls)),
    url(r'^api/', include(router.urls)),

    #AUTHENTICATION URL ENDPOINT
    url(r'^auth/', include('django.contrib.auth.urls')),
    

    # DEFAULT PROJECT URL ENDPOIUNT
    url(r'^home/', include('project.homepage.urls')),
    url(r'^about/', include('project.aboutpage.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
