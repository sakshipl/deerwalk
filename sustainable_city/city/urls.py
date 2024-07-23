from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('add/', views.add_city, name='add_city'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-cities/', views.view_citys, name='view_cities'),
]


