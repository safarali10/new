from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('logout', views.logout, name='logout'),
]



