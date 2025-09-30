from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Publications(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField(max_length=500)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_creation']  # ordre antéchronologique par défaut

    def __str__(self):
        return f"{self.auteur.username}: {self.contenu[:20]}..."
