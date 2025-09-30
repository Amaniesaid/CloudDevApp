from django import forms
from django.contrib.auth.forms import UserCreationForm
from publications.models import Publications
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),)
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('password1', 'password2')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Publications
        fields = ["contenu"]
        widgets = {
            "contenu": forms.Textarea(attrs={"rows": 3, "placeholder": "Écrivez votre message..."})
        }