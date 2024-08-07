from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('room-type', views.RoomTypeView.index, name="room_type"),
    path('get-all-room-type', views.RoomTypeView.get_all, name="get_all_room_type"),
    path('get-by-id/<id>', views.RoomTypeView.get_by_id, name="get_by_id"),
    path('room-type-save',views.RoomTypeView.save,name="save_room_type"),
    
    
    path('rooms/', views.RoomView.room_list, name='room_list'),
    path('save_room/', views.RoomView.save_room, name='save_room'),

]