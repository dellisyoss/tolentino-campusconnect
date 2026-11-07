from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Your account was created successfully! You can now log in."

class ProfileUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = get_user_model()
    form_class = ProfileForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("profile")
    success_message = "Profile updated successfully!"

    def get_object(self, queryset=None):
        return self.request.user
