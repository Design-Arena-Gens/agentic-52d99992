from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=150, unique=True)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True, default='default_team_logo.png')
    mentor = models.CharField(max_length=150)
    tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE, related_name='teams')

    players = models.ManyToManyField('players.Player', blank=True, related_name='teams')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
