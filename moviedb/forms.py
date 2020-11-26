from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, HiddenInput, forms
from .models import Movie, Review
from users.models import NewUser as User


# from django.contrib.auth import get_user_model
#
# User = get_user_model()


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {"status": HiddenInput()}


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        widgets = {
            "movie": HiddenInput(),
            "user": HiddenInput(),
            "status": HiddenInput(),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "is_manager",
            "is_superuser",
        ]
        # fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "is_manager",
        ]
        # fields = "__all__"
