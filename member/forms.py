# from django import forms
# from .models import *
# from django.contrib.auth.models import User , Group
# from django.core.exceptions import ValidationError

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     # avatar = forms.ModelChoiceField(queryset=Avatar.objects.all())
    

#     class Meta:
#         model = User
#         fields =['first_name', 'last_name' , 'username' , 'email' , 'password']

#         lable ={'password':'Password'}


#     def save(self):
#         password = self.cleaned_data.pop('password')
        
#         u = super().save()
#         u.set_password(password)
#         u.save()
#         return u