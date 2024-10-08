from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.forms import ModelForm
from mscthesis.models import Student,Status,Submission,Supervisor,Area


class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = '__all__'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length = 254, help_text= 'Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2',)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self , *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError("This user doesnot exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("This user is not active ")

        return super(UserLoginForm,self).clean(*args, **kwargs)
