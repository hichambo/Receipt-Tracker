# receipt_manager/urls.py
from django.urls import path
from .views import (
    ReceiptListView,
    AboutView,
    ReceiptDetailView,
    ReceiptCreateView,
    ReceiptUpdateView,
    ReceiptDeleteView,
    UserRegistrationView,
    CustomLoginView,
    CustomLogoutView,
)

# URL patterns for the receipt_manager app
urlpatterns = [
    # Path to display the list of receipts (ReceiptListView)
    path('', ReceiptListView.as_view(), name='receipt_list'),

    # Path to display the about page (AboutView)
    path('about/', AboutView.as_view(), name='about'),

    # Path to display the detailed view of a receipt (ReceiptDetailView)
    path('receipts/<int:pk>/', ReceiptDetailView.as_view(), name='receipt_detail'),

    # Path to display the form for creating a new receipt (ReceiptCreateView)
    path('receipts/new/', ReceiptCreateView.as_view(), name='receipt_new'),

    # Path to display the form for editing an existing receipt (ReceiptUpdateView)
    path('receipts/edit/<int:pk>/', ReceiptUpdateView.as_view(), name='receipt_edit'),

    # Path to delete an existing receipt (ReceiptDeleteView)
    path('receipts/delete/<int:pk>/', ReceiptDeleteView.as_view(), name='receipt_delete'),

    # Path to display the login form (CustomLoginView)
    path('login/', CustomLoginView.as_view(), name='login'),

    # Path to display the registration form (UserRegistrationView)
    path('register/', UserRegistrationView.as_view(), name='register'),

    # Path to handle user logout (CustomLogoutView)
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
