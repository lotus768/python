from django import forms
from .pqrsf import pqrsf


class ContacForm(forms.Form):
    nombre = forms.CharField(label="Introduzca su nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu nombre completo'}))
    correo = forms.EmailField(label="Dirección de correo", required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Escribe tu Correo Electronico'}))
    asunto = forms.ChoiceField(label="Ingresar Asunto", required=True, choices= pqrsf, widget=forms.Select(attrs={'class':'form-control'}) )
    mensaje = forms.CharField(label="Ingresar mensaje", required=True,widget=forms.Textarea(attrs={'class':'form-control different-control w-100','cols':'30','rows':'5','placeholder':'Escribe tu mensaje'}))                               
    