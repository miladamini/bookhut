from django.urls import path
from . import views

app_name = 'acoont'
urlpatterns = [
    path('register', views.registerViwe.as_view(), name='register'),
    path('check', views.checkotpViwe.as_view(), name='check_otp'),
    path('logout', views.logout_user, name='logout'),
    path('login', views.User_Login.as_view(), name='login'),

]
