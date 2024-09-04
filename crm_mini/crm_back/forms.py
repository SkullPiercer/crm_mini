from django import forms
from .models import Group, Student

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('time',)


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'age', 'parents')

    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        group = kwargs.pop('group', None)
        super().__init__(*args, **kwargs)
        if group:
            self.fields['group'].initial = group

