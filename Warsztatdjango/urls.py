"""Warsztatdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from warsztat import views

urlpatterns = [
    path('', views.RoomListView.as_view(), name='RoomList'),
    path('room/new/', views.AddRoomView.as_view(), name='AddRoom'),
    path('room/delete/<int:room_id>/', views.DeleteRoomView.as_view(), name="DeleteRoom"),
    path('room/modify/<int:room_id>/', views.ModifyRoomView.as_view(), name="ModifyRoom"),
    path('room/reserve/<int:room_id>/', views.ReserveRoomView.as_view(), name="ReserveRoom"),
    path('room/<int:room_id>/', views.RoomDetailsView.as_view(), name="RoomDetails"),
    path('search/', views.SearchView.as_view(), name="RoomList"),

]
