from django.urls import path
from .views import (
    register_view,
    login_view,
    check_username_availability,
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check-username/', check_username_availability, name='check_username'),
]
