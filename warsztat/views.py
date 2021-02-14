from django.shortcuts import render, redirect
from django.views import View
from warsztat.models import Room, Reservation
import datetime


def index(request):
    return render(request, 'index.html')


class AddRoomView(View):

    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        name = request.POST.get('room_name')
        capacity = request.POST.get('room_capacity')
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get('projector')

        if not name:
            return render(request, 'add_room.html', context={'Error': 'Room name is empty'})
        if capacity < 0:
            return render(request, 'add_room.html', context={'Error': 'Room capacity must be even'})
        if Room.objects.filter(name=name).first():
            return render(request, 'add_room.html', context={'Error': 'Room with this name already exists'})

        Room.objects.create(name=name, capacity=capacity, projector_availability=projector)
        return redirect('RoomList')


class RoomListView(View):

    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'rooms.html', context={'rooms': rooms})


class DeleteRoomView(View):

    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        room.delete()
        return redirect('RoomList')


class ModifyRoomView(View):

    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        return render(request, 'modify_room.html', context={'room': room})

    def post(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        name = request.POST.get('room_name')
        capacity = request.POST.get('room_capacity')
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get('projector')

        if not name:
            return render(request, 'modify_room.html', context={'Error': 'Room name is empty'})
        if capacity < 0:
            return render(request, 'modify_room.html', context={'Error': 'Room capacity must be even'})
        if Room.objects.filter(name=name).first():
            return render(request, 'modify_room.html', context={'Error': 'Room with this name already exists'})

        room.name = name
        room.capacity = capacity
        room.projector_availability = projector
        room.save()
        return redirect('RoomList')


class ReserveRoomView(View):

    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        return render(request, 'reservation.html', context={'room': room})

    def post(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        date = request.POST.get('reservation_date')
        comment = request.POST.get('comment')

        if Reservation.objects.filter(room=room, date=date):
            return render(request, 'reservation.html', context={'room': room, 'error': 'Room is reserved'})
        if date < str(datetime.date.today()):
            return render(request, 'reservation.html', context={'room': room, 'error': 'Date is wrong, look further!'})

        Reservation.objects.create(room=room, date=date, comment=comment)
        return redirect('RoomList')
