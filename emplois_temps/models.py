from django import forms
from django.db import models
from departement.models import Filiere
from dataclasses import dataclass, field
from django.utils.translation import gettext_lazy as _
# # Create your models here.


class Salle(models.Model):
    id_salle = models.AutoField(primary_key= True)
    salle = models.CharField(max_length=100)
    departement = models.ForeignKey("departement.Departement", default=1, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.salle)
    
 

      
class Niveau(models.Model):
    niveau = models.CharField(max_length=100)
    filiere = models.ManyToManyField(Filiere)
    def __str__(self):
        return str(self.niveau)
    


class Cour(models.Model):
    id_cour = models.AutoField(primary_key= True)
    cour = models.CharField(max_length=100)
    niveau = models.ForeignKey("Niveau",default=1, blank=False, on_delete=models.CASCADE)
    #class Meta:
        # rendre les trois clés en une clée unique  avec l'appuis de db_index=True dans les champs concernés
        #unique_together = ("cour", "niveau")
        
    def __str__(self):
        return str(self.cour)
    
    


class Seance_cour(models.Model):
    id_seance_cour = models.AutoField(primary_key= True)
    filiere = models.ForeignKey('departement.Filiere', blank=False, db_index=True, on_delete=models.CASCADE)
    salle = models.ForeignKey("Salle", blank=False, db_index=True, on_delete=models.CASCADE)
    enseignant = models.ForeignKey("utilisateurs.Enseignant", blank=False, db_index=True, on_delete=models.CASCADE)
    date_debut = models.DateTimeField(null=True, blank=True, db_index=True  )
    date_fin = models.DateTimeField(null=True, blank=True, db_index=True)
    niveau = models.ForeignKey("Niveau",blank=False, on_delete=models.CASCADE)
    cour = models.ForeignKey("Cour", blank=False, on_delete=models.CASCADE)
    color = 'red'
    seance_type = 'CM'
   
    class Meta:
        db_table = "tblevents"
        # rendre les trois clés en une clée unique  avec l'appuis de db_index=True dans les champs concernés
        unique_together = ("salle","date_debut","date_fin")
        unique_together = ("enseignant","date_debut","date_fin")
    def __str__(self):
        return str( '{0}_{1}_{2}_{3}'.format(self.enseignant, self.filiere, self.niveau, self.cour))
      
    

    
    
# class List_cour(models.Model):                                                                         
#     id_list = models.AutoField(primary_key= True)
#     courName = models.CharField(max_length=100)
#     def __str__(self):                                                                                              
#         return str(self.courName)
    
# class Groupe(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return str(self.name)
    
class Group_td(models.Model):
    id_goup = models.AutoField(primary_key= True)
    niveau = models.ManyToManyField(Niveau)
    groupe = models.CharField(max_length=100)
    def __str__(self):
        return str( self.groupe)
    
# str( '{0}_{1}'.format(self.groupe,self.niveau))   

class Seance_TD(models.Model):
    id_seance_td = models.AutoField(primary_key= True)
    filiere = models.ForeignKey('departement.Filiere', blank=False, db_index=True, on_delete=models.CASCADE)
    salle = models.ForeignKey("Salle", blank=False, db_index=True, on_delete=models.CASCADE)
    enseignant = models.ForeignKey("utilisateurs.Enseignant",  blank=False, db_index=True, on_delete=models.CASCADE)
    date_debut = models.DateTimeField(null=True, blank=True, db_index=True  )
    date_fin = models.DateTimeField(null=True, blank=True, db_index=True)
    niveau = models.ForeignKey("Niveau",blank=False, on_delete=models.CASCADE)
    cour = models.ForeignKey("Cour", blank=False,  on_delete=models.CASCADE)
    group_td = models.ForeignKey("Group_td",   blank=False, on_delete=models.CASCADE)
    color = 'black'
    seance_type = 'TD'
    
    class Meta:
        # rendre les trois clés en une clée unique  avec l'appuis de db_index=True dans les champs concernés
        unique_together = ("salle","date_debut","date_fin")
        unique_together = ("enseignant","date_debut","date_fin")
        
    def __str__(self):
        return str( '{0}_{1}_{2}_{3}_{4}'.format(self.enseignant, self.filiere, self.niveau, self.cour, self.group_td))
      
      