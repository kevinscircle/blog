from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm 
)

from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ("email", )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields