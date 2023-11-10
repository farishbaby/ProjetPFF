from django import forms
from asa_app.models import Region, Culture, Periode, Donnees, SuperUtilisateur
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = "__all__"

class CultureForm(forms.ModelForm):
    class Meta:
        model = Culture
        fields = "__all__"

class PeriodeForm(forms.ModelForm):
    class Meta:
        model = Periode
        fields = "__all__"

class DonneesForm(forms.ModelForm):
    class Meta:
        model = Donnees
        fields = "__all__"

class SuperUtilisateurForm(forms.ModelForm):
    class Meta:
        model = SuperUtilisateur
        fields = "__all__"

class ConnexionForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput)

class ContactForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=100, required=True)
    email = forms.EmailField(label="Adresse e-mail", required=True)
    sujet = forms.CharField(label="Sujet", max_length=100, required=True)
    message = forms.CharField(label="Message", widget=forms.Textarea, required=True)