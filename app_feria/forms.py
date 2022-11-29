from distutils.command.upload import upload
from tkinter import CASCADE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import User

from app_feria.models import Imagen
"""
from app_feria.models import Avatar, Imagen"""







class FormuJean(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Hombre/Mujer'}))
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuRemera(forms.Form):
    imagen = forms.ImageField(required=False)#blank=True
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Hombre/Mujer'}))
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]


class FormuCamisa(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Hombre/Mujer'}))
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuCampera(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Hombre/Mujer'}))
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuTodo100(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Hombre/Mujer'}))
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuCalzado(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Hombre/Mujer'}))
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuInvernal(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Hombre/Mujer'}))
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuPantalon(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'placeholder':'Hombre/Mujer'}))
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormularioRegistro(UserCreationForm):
    password1 = forms.CharField(label='Ingrese contraseña:', widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))
    password2 = forms.CharField(label=' Repita contraseña:', widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))

    class Meta:

        model = User
        fields = ["username","password1","password2"]

class FormularioEditarUsuario(UserCreationForm):
    email = forms.EmailField(label='Ingrese email',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    first_name= forms.CharField(label='Ingrese nombre',widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    last_name= forms.CharField(label='Ingrese apellido',widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
    password1 = forms.CharField(label='Ingrese la contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Nueva contraseña'}))
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Repita contraseña'}))

    class Meta:

        model = User
        fields = ["first_name","last_name","email","password1","password2"]
