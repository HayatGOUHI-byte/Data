from django.db import models


# Create your models here.


#Le Produit
class Produit(models.Model):
    code_produit = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs selon les besoins (par exemple, catégorie, quantité en stock, etc.)

    def __str__(self):
        return self.nom



#Client
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    adresse = models.TextField()
    # Ajoutez d'autres champs selon les besoins (par exemple, numéro de téléphone, etc.)

    def __str__(self):
        return self.nom


#Commmande

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit)
    date_commande = models.DateTimeField(auto_now_add=True)
    # Ajoutez d'autres champs selon les besoins (par exemple, statut de la commande, adresse de livraison, etc.)

    def __str__(self):
        return f"Commande de {self.client} le {self.date_commande}"


class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    annee_fabrication = models.DateTimeField()




    def __str__(self):
        return f"voiture {self.marque}"





