from django.contrib import admin
from django.urls import path


class CustomAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin'
    index_title = 'Welcome to My Custom Admin Dashboard'
    site_title = 'My Custom Admin Site'


custom_admin_site = CustomAdminSite(name='custom_admin_templates')


