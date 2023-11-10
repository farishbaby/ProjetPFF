from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Region(models.Model):
    Id_region = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100)
    Cultures = models.ManyToManyField('Culture')

    def __str__(self):
        return self.Nom
    
    class Meta:
        db_table = "Region"

class Culture(models.Model):
    Id_culture = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=100) 
    Periodes = models.ManyToManyField('Periode')
    


    def __str__(self):
        return self.Nom
    
    class Meta:
        db_table = "Culture"

class Periode(models.Model):
    Id_periode = models.AutoField(primary_key=True)
    Debut = models.DateField(auto_now=False, auto_now_add=False)
    Fin = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.Debut} - {self.Fin}"
    
    class Meta:
        db_table = "Periode"

class Donnees(models.Model):
    Id_donnees = models.AutoField(primary_key=True)
    Titre = models.CharField(max_length=50)
    Description = models.CharField(max_length=500)
    Date_donnees = models.DateField()
    Date_enregistrement = models.DateField(auto_now=True)
    Fichier = models.FileField(upload_to="data")

    def __str__(self):
        return self.Titre
    
    class Meta:
        db_table = "Donnees"

class SuperUtilisateur(models.Model):
    Id_utilisateur = models.AutoField(primary_key=True)
    Prenom = models.CharField(max_length=50)
    Nom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=250, unique=True)
    Mot_de_passe = models.CharField(max_length=50)
    Confirme_MDP = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Prenom} - {self.Nom}"
    
    class Meta:
        db_table = "SuperUtilisateur"
    