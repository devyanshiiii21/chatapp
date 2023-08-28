from django.shortcuts import render
from .models import Rooms, Message
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
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'rooms/room_detail.html', {
        'room': room,
        'messages':messages
    })