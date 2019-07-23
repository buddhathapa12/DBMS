from django import forms
from django.forms import ModelForm
from mscthesis.models import Student,Status,Submission,Supervisor,Area

class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = '__all__'