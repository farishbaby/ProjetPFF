from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('indexpro/', views.indexpro, name='indexpro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboardpro/', views.dashboardpro, name='dashboardpro'),
    path('recommandation/', views.recommandation, name='recommandation'),
    path('contact/', views.contact, name='contact'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion')
]