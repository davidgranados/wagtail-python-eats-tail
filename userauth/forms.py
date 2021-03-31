from django import forms
from wagtail.users.forms import UserCreationForm, UserEditForm

from .models import CustomUser


class WagtailUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        widgets = {"date_of_birth": forms.DateInput(attrs={"type": "date"})}


class WagtailUserEditForm(UserEditForm):
    class Meta(UserEditForm.Meta):
        model = CustomUser
        widgets = {"date_of_birth": forms.DateInput(attrs={"type": "date"})}
