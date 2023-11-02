from django.db import models
from django.contrib.auth.models import User

class ApartmentManager(models.Manager):
    def create_apartment(self, user, name, location):
        return self.create(user=user, name=name, location=location)

class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    objects = ApartmentManager()

    def __str__(self):
        return self.name

class RoomManager(models.Manager):
    def create_room(self, apartment, room_type, name):
        return self.create(apartment=apartment, room_type=room_type, name=name)

class Room(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    objects = RoomManager()

    def __str__(self):
        return self.name

class ReservationManager(models.Manager):
    def create_reservation(self, room, user, start_date, end_date):
        return self.create(room=room, user=user, start_date=start_date, end_date=end_date)

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    objects = ReservationManager()

    def __str__(self):
        return self.room.name
