from .models import RegisterUser
from django import forms

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
        fields = ['name_of_student','cell_phone','email_field','faculty','department_graduated_from','home_address','motivation']
