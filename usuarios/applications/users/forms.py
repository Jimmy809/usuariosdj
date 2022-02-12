from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placerholder': 'Contraseña'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placerholder': 'Repetir Contraseña'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'username', 
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseña no son iguales')
# agregar que no sea menor a 5 caracteres
