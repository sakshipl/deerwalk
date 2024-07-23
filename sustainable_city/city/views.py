from django.shortcuts import render, redirect
from .forms import CityForm
from .models import City
from django.contrib.auth.decorators import user_passes_test

def admin_required(user):
    return user.is_superuser

def home(request):
    return render(request, 'home.html')

@user_passes_test(admin_required)
def custom_admin_dashboard(request):
    return render(request, 'custom_admin_templates/custom_admin_dashboard.html')

@user_passes_test(admin_required)
def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_dashboard')
    else:
        form = CityForm()
    return render(request, 'custom_admin_templates/add_city.html', {'form': form})

@user_passes_test(admin_required)
def manage_users(request):
    return render(request, 'custom_admin_templates/manage_users.html')

@user_passes_test(admin_required)
def view_citys(request):
    cities = City.objects.all()
    return render(request,'custom_admin_templates/dashboard.html', {'cities': cities})