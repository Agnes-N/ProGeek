from django import forms
from .models import Programmers_profile,Project

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','programmers']