# Import necessary modules
from django.contrib import admin
from django.urls import include, path

# Define URL patterns
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include Django built-in authentication URLs (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Include custom application URLs for user authentication and receipts management
    path("accounts/", include("receipt_manager.urls")),
    
    # Include custom application URLs for receipts management
    path('', include('receipt_manager.urls')),
]
