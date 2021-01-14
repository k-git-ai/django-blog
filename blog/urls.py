from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('post/', views.post, name='blog-post'),
    path('login/', views.login, name='blog-login'),
    path('register/', views.register, name='blog-register'),
]