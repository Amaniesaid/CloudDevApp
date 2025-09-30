from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Publications
from forms import MessageForm

@login_required
def liste_messages(request):
    messages_list = Publications.objects.all()
    paginator = Paginator(messages_list, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "publications.html", {"page_obj": page_obj})

@login_required
def ajouter(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            nouveau_message = form.save(commit=False)
            nouveau_message.auteur = request.user
            nouveau_message.save()
            return redirect("liste_messages")
    else:
        form = MessageForm()
    return render(request, "ajouter_publication.html", {"form": form})

