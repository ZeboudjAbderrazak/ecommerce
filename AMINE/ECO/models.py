from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    numero_telephone = models.CharField(max_length=20)
    adresse_livraison = models.TextField()
    adresse_facturation = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Marque(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    quantite_stock = models.IntegerField(default=0)
    url_image = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.PROTECT)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=10, choices=[('En attente', 'En attente'), ('Expédiée', 'Expédiée'), ('Livrée', 'Livrée'), ('Annulée', 'Annulée')], default='En attente')
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)

class ArticleCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

class Avis(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

class PanierAchats(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

class ArticlePanier(models.Model):
    panier = models.ForeignKey(PanierAchats, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    quantite = models.IntegerField()

class Paiement(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.PROTECT)
    date_paiement = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    methode_paiement = models.CharField(max_length=20, choices=[('Carte de crédit', 'Carte de crédit'), ('PayPal', 'PayPal'), ('Autre', 'Autre')])
    statut = models.CharField(max_length=10, choices=[('En attente', 'En attente'), ('Terminé', 'Terminé'), ('Échoué', 'Échoué')], default='En attente')

class Livraison(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    adresse_livraison = models.TextField()
    methode_livraison = models.CharField(max_length=100)
    date_livraison = models.DateTimeField(auto_now_add=True)
    date_arrivee_estimee = models.DateTimeField()
    numero_suivi = models.CharField(max_length=100)

class ListeSouhaits(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

class ArticleListeSouhaits(models.Model):
    liste_souhaits = models.ForeignKey(ListeSouhaits, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
