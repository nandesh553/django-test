from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'company')


class CustomUserChangeForm(ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')