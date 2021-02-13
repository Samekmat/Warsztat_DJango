from django.shortcuts import render, redirect
from django.views import View
from warsztat.models import Room

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
        return redirect('index')
