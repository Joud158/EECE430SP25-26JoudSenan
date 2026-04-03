from django.contrib import messages
from django.db import DatabaseError
from django.shortcuts import get_object_or_404, redirect, render
from .forms import VoleyPlayerForm
from .models import VoleyPlayer


def player_list(request):
    try:
        players = VoleyPlayer.objects.all().order_by('id')
    except DatabaseError:
        messages.error(request, 'Could not load players from the database.')
        players = []
    return render(request, 'players/player_list.html', {'players': players})


def player_create(request):
    if request.method == 'POST':
        form = VoleyPlayerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Player added successfully.')
                return redirect('player_list')
            except DatabaseError:
                messages.error(request, 'A database error happened while adding the player.')
            except Exception:
                messages.error(request, 'An unexpected error happened while adding the player.')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = VoleyPlayerForm()
    return render(request, 'players/player_form.html', {'form': form, 'title': 'Add Player'})


def player_update(request, pk):
    player = get_object_or_404(VoleyPlayer, pk=pk)
    if request.method == 'POST':
        form = VoleyPlayerForm(request.POST, instance=player)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Player updated successfully.')
                return redirect('player_list')
            except DatabaseError:
                messages.error(request, 'A database error happened while updating the player.')
            except Exception:
                messages.error(request, 'An unexpected error happened while updating the player.')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = VoleyPlayerForm(instance=player)
    return render(request, 'players/player_form.html', {'form': form, 'title': 'Update Player'})


def player_delete(request, pk):
    player = get_object_or_404(VoleyPlayer, pk=pk)
    if request.method == 'POST':
        try:
            player.delete()
            messages.success(request, 'Player deleted successfully.')
        except DatabaseError:
            messages.error(request, 'A database error happened while deleting the player.')
        except Exception:
            messages.error(request, 'An unexpected error happened while deleting the player.')
        return redirect('player_list')
    return render(request, 'players/player_delete.html', {'player': player})
