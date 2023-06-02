from django.urls import path
from .views import HomePage, Donnee

urlpatterns = [
    path('', HomePage, name='accueil'),
    path('Donnees/', Donnee, name='data')
]
