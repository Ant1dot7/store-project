from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [

    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
    path('verify/<str:email>/<uuid:code>/', views.EmailVerificationView.as_view(), name='email_verification'),

]
