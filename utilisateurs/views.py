from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout,authenticate
from django.urls import reverse_lazy, reverse
from utilisateurs.models import Enseignant, Secretaire, SecretaireAdditional, EnseignantAdditional, User
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import RegistrationFormSecretaire, RegistrationFormSecretaire2, RegistrationForm, RegistrationFormEnseignant, RegistrationFormEnseignant2
from django.views.generic import TemplateView, FormView, CreateView , ListView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from emplois_temps.models import Seance_cour, Seance_TD
from utilisateurs.models import Enseignant ,Secretaire, Departement,Etab_orig 
from emplois_temps.models import Niveau, Group_td, Cour
from departement.models import Departement,Filiere


# Create your views here.


User = get_user_model()


# class RegisterViewSecretaire(CreateView):
#     template_name = "emplois_temps/registersecretaire.html"
#     form_class = RegistrationFormSecretaire
#     success_url = reverse_lazy('login')
    
#     def post(self, request, *args , **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == 302:
#             departement = request.POST.get('departement')
#             user = User.objects.get(email = request.POST.get('email'))
#             s_add=SecretaireAdditional.objects.create(user = user, departement = departement)
            
            
#             return response
#         else:
#             return response
    
# def RegisterViewSecretaire(request):
#     form = RegistrationFormSecretaire()
#     if request.method == 'POST':
#         form = RegistrationFormSecretaire(data=request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             form.save()
#             messages.success(request, "votre compte a ete birn creer")
#             return redirect('login')
#         else:
#             messages.error(request, form.errors)
#     return render(request, 'emplois_temps/registersecretaire.html', {'form':form})
        
  
class RegisterViewSecretaire(CreateView): 
    model = User
    form_class = RegistrationFormSecretaire
    template_name = "emplois_temps/registersecretaire.html"
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')    

        
                    
class RegisterViewEnseignant(CreateView):
    template_name = "emplois_temps/registerenseignant.html"
    form_class = RegistrationFormEnseignant
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')          
            


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if user.type == User.Types.SECRETAIRE :
                    return redirect('programmeseance1')
                
                else:
                    return redirect('welcomeenseignant1')
                    
                    
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'emplois_temps/login.html',
    context={'form':AuthenticationForm()})
    
    
    


def index(request):
    return render(request, "emplois_temps/index.html")

@login_required
def welcomeSecretaire(request):
    user = User.objects.get(id=request.user.id)
    return render(request, "emplois_temps/secretaire/welcomesecretaire.html", {'user':user})

@login_required
def welcomeEnseignant(request):
    return render(request, "emplois_temps/enseignant/welcomeenseignant.html")

def welcomeEnseignant1(request):
    user = User.objects.get(id=request.user.id)
    seance_cours = Seance_cour.objects.all()
    seance_TDs = Seance_TD.objects.all()
    departements = Departement.objects.all()
    enseignants = Enseignant.objects
    niveaux = Niveau.objects
    seanceTDs = Seance_TD.objects
    group_tds = Group_td.objects
    filieres = Filiere.objects
    cours = Cour.objects
    return render(request, "emplois_temps/enseignant/welcomeenseignant1.html", {'user':user, 'seance_cours':seance_cours, 'seance_TDs':seance_TDs, 'enseignants':enseignants, 'departements':departements, 'niveaux':niveaux,'seanceTDs':seanceTDs,'group_tds':group_tds, 'filieres':filieres, 'cours':cours})
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')