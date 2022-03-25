from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/accounts/signup
    path('signup', views.signup, name='signup'),
    # http://127.0.0.1:8000/accounts/login
    path('login', views.login, name='login'),
    # http://127.0.0.1:8000/accounts/logout
    path('logout', views.logout, name='logout'),
    #path('<int:blog_id>/', views.detail, name='detail'),
]
