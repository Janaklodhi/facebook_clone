from django.urls import path
from . import views

# from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    # Other URL patterns
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    # path('signup-success/', views.signup_success, name='signup_success'),    
    
]
