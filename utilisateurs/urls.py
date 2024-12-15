from django.urls import path
from utilisateurs import views
urlpatterns = [
    
    path('', views.login_request),
    path('signupsecretaire/', views.RegisterViewSecretaire.as_view(), name="signupsecretaire"),
    path('login/', views.login_request, name="login"),
    path('signupenseignant/', views.RegisterViewEnseignant.as_view(), name="signupenseignant"),
    path('welcomesecretaire/', views.welcomeSecretaire, name="welcomesecretaire"),
    path('welcomeenseignant/', views.welcomeEnseignant, name="welcomeenseignant"),
    path('welcomeenseignant1/', views.welcomeEnseignant1, name="welcomeenseignant1"),
    path('logout/',views.logout_view, name='logout'),
]
