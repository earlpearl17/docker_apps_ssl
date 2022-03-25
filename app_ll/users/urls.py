"""Defines URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login page -> http://localhost:8000/users/login/
    url(r'^login/$', login, {'template_name': 'users/login.html'},name='login'),
    
    # Logout page -> http://localhost:8000/users/logout/
    url(r'^logout/$', views.logout_view, name='logout'),
    
    # Registration page -> http://localhost:8000/users/register/
    url(r'^register/$', views.register, name='register'),
]
