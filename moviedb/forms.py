from django.forms import ModelForm,HiddenInput
from .models import Movie, Review

from django.contrib.auth import get_user_model

User = get_user_model()


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'status': HiddenInput()
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'movie': HiddenInput(),
            'user': HiddenInput(),
            'status': HiddenInput()
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
