from django import forms
from .models import Player
from tournaments.models import Tournament


class PlayerRegistrationForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tournament_consent = forms.ModelChoiceField(
        queryset=Tournament.objects.all(), required=False, empty_label="Select a tournament (optional)"
    )

    class Meta:
        model = Player
        fields = [
            'name', 'date_of_birth', 'gender', 'category', 'playing_position',
            'photo', 'institution_name', 'tournament_consent'
        ]
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
