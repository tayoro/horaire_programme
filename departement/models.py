from django.db import models

# Create your models here.
class Departement(models.Model):
    id_ufr = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
class Filiere(models.Model):
    id_filiere = models.AutoField(primary_key=True)
    departement = models.ForeignKey("Departement", default=1, blank=False, on_delete=models.CASCADE)
    filiere = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.filiere}"