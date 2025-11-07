from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .forms import PlayerRegistrationForm
from .models import Player
from teams.models import Team


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save()
            messages.success(request, f"Registration successful! Your 4-digit number is {player.registration_number}. Please note it for future reference.")
            return redirect('players:register_success', code=player.registration_number)
    else:
        form = PlayerRegistrationForm()
    return render(request, 'players/register.html', {'form': form})


def register_success(request: HttpRequest, code: str) -> HttpResponse:
    player = get_object_or_404(Player, registration_number=code)
    return render(request, 'players/register_success.html', {'player': player})


def search(request: HttpRequest) -> HttpResponse:
    return render(request, 'players/search.html')


def search_result(request: HttpRequest) -> HttpResponse:
    code = request.GET.get('code', '').strip()
    player = Player.objects.filter(registration_number=code).first()
    teams = Team.objects.filter(players=player) if player else Team.objects.none()
    return render(request, 'partials/player_detail.html', {'player': player, 'teams': teams})
