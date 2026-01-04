from django.contrib import admin
from django.urls import path, include
from accounts.views import register_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Built-in Auth URLs (Login, Logout, Password Reset)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Custom Views
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    
    # Redirect root URL (http://127.0.0.1:8000/) to dashboard
    path('', dashboard_view, name='home'), 
]