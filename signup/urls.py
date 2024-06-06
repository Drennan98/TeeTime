from django.urls import path
from .views import Signup

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]