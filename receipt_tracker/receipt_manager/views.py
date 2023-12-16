# receipt_manager/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Receipt
from .forms import ReceiptForm

# View for the About page
class AboutView(TemplateView):
    template_name = 'about.html'

# View for displaying a list of receipts (requires user login)
class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = 'receipt_list.html'
    context_object_name = 'receipts'

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)

# View for displaying detailed information about a receipt (requires user login)
class ReceiptDetailView(LoginRequiredMixin, DetailView):
    model = Receipt
    template_name = 'receipt_detail.html'
    context_object_name = 'receipt'

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)

# View for creating a new receipt (requires user login)
class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipt_form.html'
    success_url = reverse_lazy('receipt_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# View for updating an existing receipt (requires user login)
class ReceiptUpdateView(LoginRequiredMixin, UpdateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipt_form.html'
    success_url = reverse_lazy('receipt_list')

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)


class ReceiptDeleteView(LoginRequiredMixin, DeleteView):
    model = Receipt
    success_url = reverse_lazy('receipt_list')  # Redirect to the list view after deletion
    template_name = 'receipt_delete.html'  # You can create a confirmation template if needed

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)
# View for user registration
class UserRegistrationView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

# Custom logout view (requires user login)
class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'registration/logout.html'
