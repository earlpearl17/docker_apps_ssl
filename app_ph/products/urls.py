from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/products/create
    path('create', views.create, name='create'),
    # http://127.0.0.1:8000/products/<int>
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]
