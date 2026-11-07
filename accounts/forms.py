from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            classes = field.widget.attrs.get("class", "").split()
            if "form-control" not in classes:
                classes.append("form-control")
            field.widget.attrs["class"] = " ".join(classes)


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")


class BootstrapAuthenticationForm(BootstrapFormMixin, AuthenticationForm):
    pass


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email")
