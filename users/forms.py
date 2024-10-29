from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixin
from users.models import User


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserProfileUpdateForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()