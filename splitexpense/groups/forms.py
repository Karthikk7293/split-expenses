# groups/forms.py

from django import forms
from .models import Groups, GroupMember

class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'image']

class GroupMemberForm(forms.ModelForm):
    class Meta:
        model = GroupMember
        fields = ['user']
