from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction
User = get_user_model()



from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Enseignant, Secretaire, SecretaireAdditional, EnseignantAdditional, Grade, Departement, Etab_orig
from django import forms
from django.core.validators import RegexValidator

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)



class RegistrationForm(UserCreationForm):
    class Meta:
        model = Secretaire
        fields = [
            'first_name',
            'last_name',
            'email',
        
            'phone',
            'password1',
            'password2',
        ]

# class RegistrationFormSecretaire(UserCreationForm):
#     departement = forms.ModelChoiceField(queryset=Departement.objects.all())
#     class Meta:
#         model = Secretaire
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#            
#             'phone',
#             'password1',
#             'password2',
#             'departement',
#         ]


class RegistrationFormSecretaire(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    # email , password1 et password2 sont deja inclu dans "UserCreationForm"

    departement = forms.ModelChoiceField(queryset=Departement.objects.all(), required=True)
    
    class Meta(UserCreationForm.Meta):
        model = Secretaire
          
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        
        secretaireAdditional = SecretaireAdditional.objects.create(user=user)
        secretaireAdditional.departement = self.cleaned_data.get('departement')
        secretaireAdditional.save()
        return user
        
        
        
        
class RegistrationFormSecretaire2(forms.ModelForm):
    class Meta:
        model = SecretaireAdditional
        fields = [
            'departement'
        ]



# class RegistrationFormEnseignant(UserCreationForm):
#     grade = forms.ModelChoiceField(queryset=Grade.objects.all())
#     etab_orig = forms.ModelChoiceField(queryset=Etab_orig.objects.all())
#     class Meta:
#         model = Enseignant
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
           
#             'phone',
#             'password1',
#             'password2',
#             'grade',
#             'etab_orig',
            
#         ]
        

    
class RegistrationFormEnseignant(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    
    # email , password1 et password2 sont deja inclu dans "UserCreationForm"
    
    grade = forms.ModelChoiceField(queryset=Grade.objects.all())
    etab_orig = forms.ModelChoiceField(queryset=Etab_orig.objects.all())
    
    class Meta(UserCreationForm.Meta):
        model = Enseignant
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        
        enseignantAdditional = EnseignantAdditional.objects.create(user=user)
        enseignantAdditional.grade = self.cleaned_data.get('grade')
        enseignantAdditional.etab_orig = self.cleaned_data.get('etab_orig')
        enseignantAdditional.save()
        return user
        
       
       
       
class RegistrationFormEnseignant2(UserCreationForm):
    class Meta:
        model = EnseignantAdditional
        fields = [
            'grade',
            'etab_orig',
            'departement',
        ]
        

class SendOtpBasicForm(forms.Form):
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = forms.CharField(max_length=255, validators=[phone_regex])

    class Meta:
        fields = [
            'phone',
        ]


class VerifyOtpBasicForm(forms.Form):
    otp_regex = RegexValidator( regex = r'^\d{4}$',message = "otp should be in six digits")
    otp = forms.CharField(max_length=6, validators=[otp_regex])

    # class Meta:
    #     field
