from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def register_view(request):
    # If user is already logged in, send them to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after registration
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard_view(request):
    # Internship Level: Demonstrating Role-Based Access Control (RBAC)
    if request.user.is_superuser:
        role = "System Administrator"
        permissions = "Full access to all modules."
    else:
        role = "Standard User"
        permissions = "Access to personal tasks only."

    context = {
        'role': role,
        'permissions': permissions
    }
    return render(request, 'dashboard.html', context)