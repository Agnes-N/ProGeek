from django import forms
from .models import Programmers_profile,Project, Chat

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','programmers']
        
class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        exclude = []