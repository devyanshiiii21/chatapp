from django.shortcuts import render
from .models import Rooms
from django.contrib.auth.decorators import login_required


@login_required
def rooms(request):
    rooms = Rooms.objects.all()

    return render(request, 'rooms/room.html', {
        'rooms': rooms
    })


@login_required
def room_detail(request, slug):
    room = Rooms.objects.get(slug = slug)

    return render(request, 'rooms/room_detail.html', {
        'room': room
    })