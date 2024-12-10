# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),  # Add this line for the login view
    path('logout/', views.logout_view, name='logout'), # Add this line for the logout view
    # Other user-related URLs
]
