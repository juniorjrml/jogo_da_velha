from django import forms

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        #field_classes = {'password': forms.PasswordInput, }
        exclude = ['is_staff', 'is_active', 'is_superuser', 'user_permissions', 'last_login', 'groups', 'date_joined']

        widgets = {'password': forms.PasswordInput}