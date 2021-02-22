from django.forms import ModelForm
from .models import ScrumyGoals
from django.contrib.auth.models import User

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'email', 'username', 'password']


class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['user', 'goal_name']