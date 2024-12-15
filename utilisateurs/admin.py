from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Enseignant, Etab_orig, Departement, Filiere, Secretaire,EnseignantSpecifique, Grade #, Salle, Seance, Cour, List_cour, Group_td, Niveau, Td, List_salle

from .forms import UserCreationForm, UserChangeForm



from django.contrib.auth.models import User

# Register your models here.

from .models import  SecretaireAdditional , EnseignantAdditional
from django.contrib import admin


User = get_user_model()


# Supprimer le modèle de groupe de l'administrateur. Nous ne l'utilisons pas.





    
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_active','is_staff','is_superuser',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','type', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone','Seance',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions',)}),   #'is_customer' , 'is_seller'
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (   'first_name','last_name','phone','email','type', 'password1', 'password2', 'is_staff', 'is_active')}
         
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()
    
     # Les formulaires pour ajouter et modifier des instances d'utilisateur
class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name','email', 'is_active','is_staff','is_superuser', ]
    list_filter = ['is_active','groups']
    filter_horizontal = ("groups", "user_permissions")
    list_filter = ('is_active',)
    search_fields = ['last_name']
    ordering = ['last_name']
    



    
class SecretaireAdditionalInline(admin.TabularInline):
    model = SecretaireAdditional

class SecretaireAdmin(admin.ModelAdmin):
    inlines = (
        SecretaireAdditionalInline,
    )
    filter_horizontal = ("groups", "user_permissions")
    list_display = ('last_name','first_name','email', 'is_active','is_staff','is_superuser',)
    list_filter = ( 'is_staff', 'is_active',)
    search_fields = ['email']
    ordering = ['email']
    
    
    

class EnseignantAdditionalInline(admin.TabularInline):
    model = EnseignantAdditional
    
    
class EnseignantAdmin(admin.ModelAdmin):
    inlines = (
        EnseignantAdditionalInline,
    )
    filter_horizontal = ("groups", "user_permissions")
    list_display = ('last_name','first_name','email', 'is_active','is_staff','is_superuser',)
    
    search_fields = ['email']
    ordering = ['email']
    


#1 using simple database for sessions 
from django.contrib.sessions.models import Session
import pprint


admin.site.register(User, UserAdmin)
#admin.site.register(Secretaire)
admin.site.register(Secretaire ,SecretaireAdmin)
admin.site.register(Enseignant ,EnseignantAdmin)
admin.site.register(EnseignantSpecifique ,EnseignantAdmin)
#admin.site.register(EnseignantAdditional)
#admin.site.register(SecretaireAdditional)
#admin.site.register(Enseignant, UserAdmin)
#admin.site.register(Secretaire, UserAdmin)
admin.site.register(Etab_orig)
admin.site.register(Departement)
admin.site.register(Filiere)
admin.site.register(Grade)