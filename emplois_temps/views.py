from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Seance_cour, Seance_TD
from utilisateurs.models import Enseignant ,Secretaire, Departement,Etab_orig 
from emplois_temps.models import Niveau, Group_td, Cour
from departement.models import Departement,Filiere
from .forms import Seance_TdForm, Seance_courForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
def classe_L1(request):
    return Seance_cour.objects.get(niveau='L1')
    
#@login_required
def programme_seance(request):
    all_events1 = Seance_cour.objects.all()
    all_events2 = Seance_TD.objects.all()
    all_events = []
    for events in all_events1 :
        all_events.append(events)
    for events in all_events2 :
        all_events.append(events)

    
    #print(departements)
    # si la requette est envoyé et qu'il existe un profil type dans la requette alors 
    if len(request.GET) > 0 and 'profileType' in request.GET:
        seanceCourForm = Seance_courForm(prefix="cr")
        seanceTdForm = Seance_TdForm(prefix="td")
        # si le profileType est une secreatire  
        
        if request.GET['profileType'] == 'cour':
            seanceCourForm = Seance_courForm(data=request.GET, prefix='cr')
            # la formulaire secreatire est valid
            if seanceCourForm.is_valid():
                
                # alors enregistrer 
                seanceCourForm.save()
                messages.success(request, "Seance cour a bien été enregistré")
                # et redirige a la page login
                return redirect('programmeseance1')
        # sinon si le profiletype est enseignant 
        elif request.GET['profileType'] == 'TD':
            seanceTdForm  = Seance_TdForm(data=request.GET, prefix='td')
            # et si la formulaire enseignant est valide alors 
            if seanceTdForm.is_valid():
                #alors enregistrer
                seanceTdForm.save()
                messages.success(request, "Seance TD a bien été enregistré")
                return redirect('programmeseance1')
        # Le formulaire n'est pas valide
        return render(request, 'emplois_temps/programmeseance1.html', {'seanceTdForm': seanceTdForm,'seanceCourForm':seanceCourForm, 'events' : all_events })
    else:
        # si la requette n'a pas pu etre envoyé 
        seanceCourForm  = Seance_courForm(prefix='cr')
        seanceTdForm = Seance_TdForm(prefix='td')
        return render(request, 'emplois_temps/programmeseance1.html',{'seanceTdForm': seanceTdForm,'seanceCourForm':seanceCourForm, 'events' : all_events})




def all_events(request):
    
    all_events1 = Seance_cour.objects.all()
    all_events2 = Seance_TD.objects.all()
    all_events = []
    for events in all_events1 :
        all_events.append(events)
    for events in all_events2 :
        all_events.append(events)
    out = []
    for event in all_events:
            if event.seance_type == 'CM':
                out.append({
                    'title' : event.cour.cour, 
                    'filiere':event.filiere.filiere,
                    'id ': event.id_seance_cour,
                    'start' :event.date_debut.strftime("%m/%d/%Y, %H:%M:%S"),
                    'end' :event.date_fin.strftime("%m/%d/%Y, %H:%M:%S"),
                    'color':event.color
                })
            else:
                out.append({
                    'title' : event.cour.cour, 
                    'filiere':event.filiere.filiere,
                    'id ': event.id_seance_td,
                    'start' :event.date_debut.strftime("%m/%d/%Y, %H:%M:%S"),
                    'end' :event.date_fin.strftime("%m/%d/%Y, %H:%M:%S"),
                    'color':event.color
                })
    
    return JsonResponse(out, safe=False)


def update_cour(request):
    
    all_events1 = Seance_cour.objects.all()
    all_events2 = Seance_TD.objects.all()
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    all_events = []
    for events in all_events1 :
        all_events.append(events)
    for events in all_events2 :
        all_events.append(events)
    
    for event in all_events:
            if event.seance_type == 'CM':
                event = Seance_cour.objects.get(id_seance_cour=id)
                event.date_debut = start
                event.date_fin = end
                event.cour.cour = title
                event.save()
            else:
                event = Seance_cour.objects.get(id_seance_td=id)
                event.start = start
                event.end = end
                event.cour.cour = title
                event.save()
            data = {}
    return JsonResponse(data)
    