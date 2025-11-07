from django.contrib import admin
from .models import Tournament


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'created_at')
    search_fields = ('name',)
