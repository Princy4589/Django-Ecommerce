from django.contrib import admin
from .models import Categorie,Produit

class AdminCategorie(admin.ModelAdmin):
    list_display=('nom_ctg','date_ajout_ctg')

class AdminProduit(admin.ModelAdmin):
    list_display=('nom_produit','date_ajout_prod','prix_produit','categorie_produit')

admin.site.register(Produit,AdminProduit)
admin.site.register(Categorie,AdminCategorie)

