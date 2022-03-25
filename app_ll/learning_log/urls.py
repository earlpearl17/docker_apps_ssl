"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # http://localhost:8000/admin/
    url(r'^admin/', include(admin.site.urls)),
    # http://localhost:8000/
    url(r'', include('learning_logs.urls', namespace='learning_logs')),
    # http://localhost:8000/users/
    # http://localhost:8000/users/login/
    url(r'^users/', include('users.urls', namespace='users')),
]
