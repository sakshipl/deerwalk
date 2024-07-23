from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .models import City, Tag, Building


def custom_admin_dashboard(request):
    return HttpResponse("<h1>Custom Admin Dashboard</h1>")


class CustomAdminSite(admin.AdminSite):
    site_header = 'Sustainable City Admin'
    index_title = 'Admin Dashboard'
    site_title = 'Sustainable City'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom_dashboard/', self.admin_view(custom_admin_dashboard))
        ]
        return custom_urls + urls


admin_site = CustomAdminSite(name='custom_admin')


admin_site.register(City)
admin_site.register(Tag)
admin_site.register(Building)


