from django import forms 
from .models import  registro 
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  

class registroForm(forms.ModelForm):  
    class Meta:  
        model =  registro 
        fields = '__all__'  


class RegistroUsuarioForm(UserCreationForm): 
    class Meta: 
        model = User 
        fields = ['username', 'password1', 'password2']  
