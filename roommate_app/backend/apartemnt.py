from django.db import models
from django.contrib.auth.models import User

class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def create_apartment(user, name, location):
        apartment = Apartment.objects.create(user=user, name=name, location=location)
        apartment.save()

    def get_user_apartments(user):
        apartments = Apartment.objects.filter(user=user)
        return apartments

    def update_apartment(apartment, name, location):
        apartment.name = name
        apartment.location = location
        apartment.save()

    def delete_apartment(apartment):
        apartment.delete()

class Room(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def create_room(apartment, room_type, name):
        room = Room.objects.create(apartment=apartment, room_type=room_type, name=name)
        room.save()

    def get_apartment_rooms(apartment):
        rooms = Room.objects.filter(apartment=apartment)
        return rooms

    def update_room(room, room_type, name):
        room.room_type = room_type
        room.name = name
        room.save()

    def delete_room(room):
        room.delete()

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.room.name

    def create_reservation(room, user, start_date, end_date):
        reservation = Reservation.objects.create(room=room, user=user, start_date=start_date, end_date=end_date)
        reservation.save()

    def get_user_reservations(user):
        reservations = Reservation.objects.filter(user=user)
        return reservations

    def update_reservation(reservation, start_date, end_date):
        reservation.start_date = start_date
        reservation.end_date = end_date
        reservation.save()

    def delete_reservation(reservation):
        reservation.delete()

