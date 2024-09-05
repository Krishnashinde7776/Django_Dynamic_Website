from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/',views.signup, name='singup'),
    path('login/',views.handleLogin, name='handlelogin'),
    path('logout/',views.handleLogout, name='handlelogout'),
]