from django.contrib import admin
from emplois_temps.models import Salle, Seance_cour, Cour, Niveau, Group_td, Seance_TD
#from emplois_temps.models import List_cour, List_salle, List_niveau, Date,
# Register your models here.
admin.site.register(Seance_cour)
admin.site.register(Niveau)
admin.site.register(Salle)
admin.site.register(Cour)
#admin.site.register(List_cour)
admin.site.register(Group_td)
admin.site.register(Seance_TD)
#admin.site.register(Groupe)
#admin.site.register(Cour_niveau)
#admin.site.register(List_salle)
#admin.site.register(Date)
#admin.site.register(List_niveau)

