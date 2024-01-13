from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('ymap/', views.ymap, name='ymap'),
    path('markers/', views.markers, name='markers'),
    path('join/', views.join, name='join'),
]
