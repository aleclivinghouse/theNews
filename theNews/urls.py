"""theNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url, include
from newsApp import views as newsApp_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', newsApp_views.home, name='home'),
    url(r'^post_list$', newsApp_views.post_list, name='post_list'),
    url(r'^author/(?P<id>\d+)$', newsApp_views.the_author, name="the_author"),
    url(r'^the_category/(?P<id>\d+)$', newsApp_views.the_category, name="the_category"),
    url(r'^story/(?P<id>\d+)$', newsApp_views.the_story, name="the_story"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
