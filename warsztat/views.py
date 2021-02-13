from django.shortcuts import render, redirect
from django.views import View
from warsztat.models import Room


class AddRoomView(View):

    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        name = request.POST.get('room_name')
        capacity = request.POST.get('room_capacity')
        projector = request.POST.get('projector')
