from django.contrib import admin
from .models import Region, Culture, Periode, Donnees, SuperUtilisateur

# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    list_display = ('Id_region', 'Nom', 'cultures_list')

    def cultures_list(self, obj):
        # Cette méthode retourne une liste concaténée des noms de cultures associées à la région.
        return ", ".join([culture.Nom for culture in obj.Cultures.all()])

admin.site.register(Region, RegionAdmin)

class CultureAdmin(admin.ModelAdmin):
    list_display = ('Id_culture', 'Nom', 'periodes_list')

    def periodes_list(self, obj):
        # Cette méthode retourne une liste concaténée des périodes associées à la culture.
        return ", ".join([str(periode) for periode in obj.Periodes.all()])

admin.site.register(Culture, CultureAdmin)

class PeriodeAdmin(admin.ModelAdmin):
    list_display = ('Id_periode', 'Debut', 'Fin')

admin.site.register(Periode, PeriodeAdmin)

class DonneesAdmin(admin.ModelAdmin):
    list_display = ('Id_donnees', 'Titre', 'Description', 'Date_donnees', 'Date_enregistrement', 'Fichier')

admin.site.register(Donnees, DonneesAdmin)

class SuperUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('Id_utilisateur', 'Prenom', 'Nom', 'Email', 'Mot_de_passe', 'Confirme_MDP')

admin.site.register(SuperUtilisateur, SuperUtilisateurAdmin)



