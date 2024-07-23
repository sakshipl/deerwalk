from django.urls import include, path
from django.contrib import admin
from city import views as city_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-admin/', include('city.urls')),
    path('accounts/', include('accounts.urls')),
    path('', city_views.home, name='home'),
]






