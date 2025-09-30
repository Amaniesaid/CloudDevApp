from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from forms import CustomUserCreationForm


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_messages')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
    return render(request, 'connexion.html')

def publications(request):
    return redirect('liste_messages')

def deconnexion(request):
    logout(request)
    return redirect('connexion')

