from argparse import Action
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from queue import Full
from .models import *
# Create your views here.


def home(req):
    return render(req,'home.html')

# app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import RoomType
from .forms import RoomTypeForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomType
from .forms import RoomTypeForm
from django.contrib import messages

def home(req):
    return render(req, 'home.html')

class RoomTypeView:
    def index(req):
        data = RoomType.objects.all()
        context = {
            'data': data
        }
        return render(req, 'room_type/index.html', context)
    
    def get_by_id(req,id):
        data = RoomType.objects.get(id=id)
        context = {
            'id':data.id,
            'name':data.name,
            'name_kh':data.name_kh
        }
        return JsonResponse({'data':context})
        
    def get_all(req):
        data = RoomType.objects.all()
        return JsonResponse({'data': list(data.values())})

    def save(req):
        room_type_id = req.POST.get("room_type_id")  
        name = req.POST.get("name")
        name_kh = req.POST.get("name_kh")
        action = req.POST.get("action")
        try:
            if action == "delete":
                room_type = get_object_or_404(RoomType,pk=room_type_id)
                room_type.delete()
                messages.success(req,"លុបទិន្នន័យដោយជោគជ័យ!")
                return redirect('room_type') 
            elif room_type_id:
                room_type = get_object_or_404(RoomType,pk=room_type_id)
                room_type.name = name
                room_type.name_kh = name_kh
                room_type.save()
                messages.success(req, "កែប្រែទិន្នន័យដោយជោជ័យ!")
                return redirect('room_type')
            else:
                room_type = RoomType(name=name,name_kh=name_kh)
                room_type.save()
                messages.success(req,"បង្កើតដោយជោគជ័យ!")
                return redirect('room_type')
            
        except Exception as e:
            messages.error(req,f"An error occurred: {str(e)}")

class RoomView:
    @staticmethod
    def room_list(request):
        rooms = Room.objects.all()
        room_types = RoomType.objects.all()
        return render(request, 'room/index.html', {'rooms': rooms, 'room_types': room_types})

    @staticmethod
    def save_room(request):
        if request.method == 'POST':
            action = request.POST.get('action')
            room_id = request.POST.get('room_id')
            room_type_id = request.POST.get('room_type_id')
            room_number = request.POST.get('room_number')
            description = request.POST.get('description')

            print("Action:", action)
            print("Room ID:", room_id)
            print("Room Type ID:", room_type_id)
            print("Room Number:", room_number)
            print("Description:", description)

            if not room_type_id:
                messages.error(request, 'Room type is required.')
                return redirect('room_list')

            if action == 'create':
                try:
                    room_type = get_object_or_404(RoomType, pk=room_type_id)
                except RoomType.DoesNotExist:
                    messages.error(request, 'Invalid Room Type.')
                    return redirect('room_list')

                Room.objects.create(room_type=room_type, room_number=room_number, description=description)
                messages.success(request, 'Room created successfully.')
            elif action == 'update':
                room = get_object_or_404(Room, pk=room_id)
                try:
                    room_type = RoomType.objects.get(pk=room_type_id)
                except RoomType.DoesNotExist:
                    messages.error(request, 'Invalid Room Type.')
                    return redirect('room_list')

                room.room_type = room_type
                room.room_number = room_number
                room.description = description
                room.save()
                messages.success(request, 'Room updated successfully.')
            elif action == 'delete':
                room = get_object_or_404(Room, pk=room_id)
                room.delete()
                messages.success(request, 'Room deleted successfully.')

        return redirect('room_list')