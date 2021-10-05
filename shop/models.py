from django.db import models

#table categories
class Categorie(models.Model):
    nom_ctg=models.CharField(max_length=200)
    date_ajout_ctg=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-date_ajout_ctg']

    def __str__(self):
            return self.nom_ctg  
        

#table produit
class Produit(models.Model):
    nom_produit=models.CharField(max_length=200)
    prix_produit=models.FloatField()
    description_produit=models.TextField()
    categorie_produit=models.ForeignKey(Categorie,related_name='categorie',on_delete=models.CASCADE)
    image_produit=models.ImageField()
    date_ajout_prod=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-date_ajout_prod']

    def __str__(self):
            return self.nom_produit    