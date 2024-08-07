from django.db import models

# Create your models here.

class RoomType(models.Model):
    class Meta:
        db_table = "room_type"
    room_type_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    name_kh = models.CharField(max_length=255)
    objects = models.Manager()
    
    def __str__(self):
        return self.name

class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return f"{self.room_number} - {self.room_type.name}"
