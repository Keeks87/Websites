from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('join_us/', views.join_us, name='join_us'),
    path('sign_up/', views.sign_up, name='sign_up'),
]
