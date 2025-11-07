from django.contrib import admin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'tournament', 'num_players')
    list_filter = ('tournament',)
    search_fields = ('name', 'mentor')
    filter_horizontal = ('players',)

    def num_players(self, obj: Team):  # type: ignore[override]
        return obj.players.count()
    num_players.short_description = 'Players'
