from django import forms
from .models import Group

class PockemonForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('time',)