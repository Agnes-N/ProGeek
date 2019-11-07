from django import forms
from .models import Programmers_profile,Project

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','programmers']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Programmers_profile
        exclude = ['user']

# class NewPartnerForm(forms.ModelForm):
#     class Meta:
#         model = Partner
#         exclude = ['user']