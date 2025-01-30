from django.urls import path
from . import views
from .views import signup_success
urlpatterns = [
    # Other URL patterns
    path('signup/', views.signup, name='signup'),
    path('signup-success/', signup_success, name='signup_success'),
    
    
]
