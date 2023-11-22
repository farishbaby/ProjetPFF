from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .forms import ConnexionForm, ContactForm
from django.conf import settings
import pdfkit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests
# Create your views here.

def index(request):
    return render(request, 'index.html')

def indexpro(request):
    
    return render(request, 'index2.html') 

def dashboard(request):
    return render(request, 'dashboard.html')

def dashboardpro(request):
    return render(request, 'dashboard2.html')

def recommandation(request):
    return render(request, 'recommandation2.html')

def contact(request):
    return render(request, 'contact2.html')

def inscription(request):
    formulaire_envoye = False
    erreur_message = ""  # Initialisez le message d'erreur vide
    if request.method == "POST":
        prenom = request.POST.get('Prenom','')
        nom = request.POST.get('Nom')
        email = request.POST.get('Email','')
        password = request.POST.get('Mot_de_passe', '')
        confirme_mdp = request.POST.get('Confirme_MDP', '')

        if not prenom or not nom or not email or not password or not confirme_mdp:
            erreur_message = "Tous les champs doivent être remplis."
        else:

            try:
                utilisateur_existant = SuperUtilisateur.objects.get(Email=email)
                erreur_message = "L'adresse e-mail existe déjà."
            except SuperUtilisateur.DoesNotExist:
                pass

            if erreur_message:
                # S'il y a une erreur, retournez à la page d'inscription
                return render(request, 'inscription.html', {'erreur_message': erreur_message})

            # Vérifiez si les mots de passe correspondent
            if password == confirme_mdp:
                # Hachez le mot de passe
                password_hacher = make_password(password)

                # Créez l'utilisateur dans la base de données avec le mot de passe haché
                utilisateur = SuperUtilisateur(Prenom=prenom, Nom=nom, Email=email, Mot_de_passe=password_hacher)
                utilisateur.save()

                # Redirigez l'utilisateur vers une page de confirmation d'inscription ou de connexion
                return redirect('/indexpro')
            else:
                # Gérez le cas où les mots de passe ne correspondent pas
                erreur_message = "Les mots de passe ne correspondent pas."
            
    # Passez le message d'erreur au modèle
    
    return render(request, 'inscription.html', {'erreur_message': erreur_message})

def connexion(request):
    erreur_message = ""
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            utilisateur = authenticate(request, email=email, password=password)

            if utilisateur is not None:
                login(request, utilisateur)

                prenom = utilisateur.Prenom
                nom = utilisateur.Nom
                
                return redirect('/indexpro')  # Redirigez vers la page de l'utilisateur connecté
            else:
                erreur_message = "Identifiants incorrects. Veuillez réessayer."
        else:
            # Gérez les erreurs de validation du formulaire
            erreur_message = "Veuillez corriger les erreurs dans le formulaire."

    else:
        form = ConnexionForm()

    return render(request, 'login.html', {'form': form, 'erreur_message': erreur_message})

def mail(request):
    subject = "Salut"
    message = "Félicitations"
    to_email = "farimatawade25@gmail.com"
    
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])
        msg = "Mail sent successfully"
    except Exception as e:
        msg = f"Mail could not be sent. Error: {e}"
        print(msg)

    return HttpResponse(msg)

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['nom']
            subject =  contact_form.cleaned_data['sujet']
            message = contact_form.cleaned_data['message']
            from_email = contact_form.cleaned_data['email']
            to_email = "farimatawade25@gmail.com"  # Utiliser l'adresse e-mail prédéfinie
            
            try:
                send_mail(subject, message, [from_email], [to_email])
                msg = "Mail sent successfully"
                return redirect('/indexpro')  # Redirigez vers la page souhaitée après l'envoi du mail
            except Exception as e:
                msg = f"Mail could not be sent. Error: {e}"
                print(msg)
    else:
        contact_form = ContactForm()

    return render(request, "contact2.html", {'form': contact_form})



# Chemin vers l'exécutable wkhtmltopdf, assurez-vous qu'il est correct
wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

# Configuration pdfkit avec le chemin vers l'exécutable wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)


def generer_rapport_powerbi(request):
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiZTlkMmYxMjAtN2ZkMS00OWZlLWE4YTQtZGY0ZGZiNmQ1ZjJhIiwidCI6ImE5ZmYwM2Q5LWMyNzMtNDdlZi05MmRkLTgzZjM5M2E4MzBhNiJ9&pageName=ReportSection462bc0b8987db68f471e"

    # Spécifiez le chemin complet du fichier PDF
    pdf_path = 'C:\\Users\\HP\\Téléchargements\\rapport_powerbi.pdf'

    # Convertir la page PowerBI directement en PDF
    pdf_content = pdfkit.from_url(powerbi_url, configuration=config)

    # Enregistrez le fichier PDF
    with open(pdf_path, 'wb') as f:
        f.write(pdf_content)

    # Créer une réponse HTTP avec le type de contenu PDF
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport_powerbi.pdf"'

    return response



            








