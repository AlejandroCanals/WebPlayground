from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

#Formulario para la Creación de Usuario
class UserCreationFormWithEmail(UserCreationForm):

    email = forms.EmailField(required=True, help_text= "Requerido, 254 caractes como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        cleaned_data = super().clean() 
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro")
        return email
    
#Formulario para la Creación de Perfil Usuario
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3' }),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3','rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3','placeholder':'Enlace'}),
            
        }

#Formulario que maneja el cambio de nombre de email
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text= "Requerido, 254 caractes como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        cleaned_data = super().clean() 
        email = cleaned_data.get("email")

        #Comprobamos si el email ha sido modificado
        if 'email' in self.changed_data:
            #Si ha sido modificado entonces comprobamos si ya existe en nuestra base de datos
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado, prueba con otro")
            
        return email

#Formulario que maneja el cambio de nombre de usuario
class UserNameForm(forms.ModelForm):
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['username']
    
    def clean_username(self):
        cleaned_data = super().clean() 
        username = cleaned_data.get("username")

        if 'username' in self.changed_data:
                    #Si ha sido modificado entonces comprobamos si ya existe en nuestra base de datos
                    if User.objects.filter(username=username).exists():
                        raise forms.ValidationError("El nombre de usario ya esta registrado, prueba con otro")
                    
        return username
    
#Formulario que maneja el cambio de contrasena

class PasswordUserForm(forms.ModelForm):
     password = forms.CharField()