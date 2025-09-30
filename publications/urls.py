from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_messages, name='liste_messages'),
    path('ajouter/', views.ajouter, name='ajouter'),
]
