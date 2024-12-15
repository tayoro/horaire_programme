from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import PermissionsMixin
from multiselectfield import MultiSelectField 
from django.contrib.auth.models import (
BaseUserManager, AbstractBaseUser
)

from departement.models import Departement , Filiere

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Crée et enregistre un utilisateur avec l'e-mail et le mot de passe donnés.
        """
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse e-mail')

        user = self.model(
        email=self.normalize_email(email),
        **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        ENSEIGNANT = 'Enseignant', 'Enseignant'
        SECRETAIRE = 'Secretaire', 'Secretaire'
        ENSEIGNANTSPECIFIQUE = 'Enseignantspecifique', 'Enseignantspecifique'
    default_type = Types.SECRETAIRE
    type = models.CharField(_("type"), max_length=225, choices=Types.choices, default=default_type)
    #type = MultiSelectField(max_length=5000, choices=Types.choices, default=[], null=True, blank=True)
    
    grade_choices = (
        ('1', 'Feminin'),
        ('2', 'Masculin'),
    )
    # blank (champ requis)
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(
    verbose_name='email address',
    max_length=255,
    unique=True,
    )
    phone = models.CharField(max_length=100, blank=False, null=True)
    #sexe = models.CharField(_("sexe"), choices = grade_choices, default=1, blank=False, max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user 
    is_superuser = models.BooleanField(default=False) # a superuser
    # remarquez l'absence du "champ password", c'est intégré pas besoin de preciser.
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password sont requis par défaut.
    def get_full_name(self):
        # L'utilisateur est identifié par son adresse e-mail
        return self.email
    def get_short_name(self):
    # L'utilisateur est identifié par son adresse e-mail
        return self.email

    def __str__(self):
        return self.last_name 
    
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
            #self.type.append(self.default_type)
        return super().save(*args, **kwargs)
    
    

    
    
class EnseignantAdditional(models.Model):
    user = models.OneToOneField(User,default="", blank=False, on_delete = models.CASCADE)
    grade = models.ForeignKey("Grade", default=1, blank=False, on_delete=models.CASCADE)
    etab_orig = models.ForeignKey("Etab_orig", default=1, blank=False, on_delete=models.CASCADE)
    departement = models.ManyToManyField(Departement)
    filiere = models.ManyToManyField(Filiere)
    


class SecretaireAdditional(models.Model):
    user = models.OneToOneField(User, default="",on_delete = models.CASCADE)
    departement = models.ForeignKey("departement.Departement", default=1, blank=False, on_delete=models.CASCADE, db_constraint=False)
    def __str__(self):
        return f"{self.departement}"

# Model Managers for proxy models
class EnseignantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type=User.Types.ENSEIGNANT))
        #return super().get_queryset(*args, **kwargs).filter(Q(type__contains=User.Types.ENSEIGNANT))
    
class EnseignantSpecifiqueManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type=User.Types.ENSEIGNANTSPECIFIQUE))
        #return super().get_queryset(*args, **kwargs).filter(Q(type__contains=User.Types.ENSEIGNANT))
        
class SecretaireManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type=User.Types.SECRETAIRE))
        #return super().get_queryset(*args, **kwargs).filter(Q(type__contains=User.Types.SECRETAIRE))


class Grade(models.Model):
    #id_grade = models.AutoField(primary_key= True)  
    grade = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.grade}"
    
class Etab_orig(models.Model):
    id_etab_orig = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
# Proxy Models. They do not create a seperate table 
class Enseignant(User):
    default_type = User.Types.ENSEIGNANT
    objects = EnseignantManager()
    class Meta:
        proxy = True
        
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.type = User.Types.ENSEIGNANT
    #         return super().save(*args, **kwargs)
        
    def enseignant(self):
        print('I can consulter')
    
    @property
    def showAdditional(self):
        return self.enseignantadditional
    
    
class EnseignantSpecifique(User):
    default_type = User.Types.ENSEIGNANTSPECIFIQUE
    objects = EnseignantSpecifiqueManager()
    class Meta:
        proxy = True
        
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.type = User.Types.ENSEIGNANT
    #         return super().save(*args, **kwargs)
        
    def enseignantSpecifique(self):
        print('I can consulter and i can programmer')
    
    @property
    def showAdditional(self):
        return self.enseignantadditional
        

class Secretaire(User):
    default_type = User.Types.SECRETAIRE
    objects = SecretaireManager()
    class Meta:
        proxy = True
        
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.type = User.Types.SECRETAIRE
    #         return super().save(*args, **kwargs)
        
    def secretaire(self):
        print('I can programmer')
        
    @property
    def showAdditional(self):
        return self.secretaireadditional



 