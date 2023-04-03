from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('forgot/',forgot_password,name='forgot'),
    path('user/<int:id>/verify',verify_otp,name='verify_otp'),
    path('user/<int:id>/change',password_change,name='password_change'),




]