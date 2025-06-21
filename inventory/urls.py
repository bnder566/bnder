from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.cars_list, name='cars_list'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
]
