from django import forms
from .models import Rooms , Participants, User

class GroupForm(forms.ModelForm):
    class Meta:
        model= Rooms
        fields='__all__'

class addOrRemoveMember(forms.ModelForm):

    # members = forms.ModelChoiceField(queryset=Rooms.objects.all())
    class Meta:
        model= Rooms
        fields= ['group_members']

   