from django.db import models

# Create your models here.


class Contact(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=40)
    numero = models.IntegerField()
    email = models.EmailField()


    def __str__(self) :
        return self.nom