from django.db import models
from django.conf import settings
class Room(models.Model):
   number = models.IntegerField()
   capacity = models.IntegerField()
   location = models.TextField()

   def __str__(self):
       return f"Room #{self.number} - {self.capacity}"

   class Meta:
       verbose_name = "Room"
       verbose_name_plural = "Rooms"
       ordering = ["number"]



class Booking(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="bookings")
   room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name="bookings")
   start_time = models.DateTimeField()
   end_time = models.DateTimeField()
   creation_time = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f"Room #{self.user.username} - {self.room}"

   class Meta:
       verbose_name = "Booking"
       verbose_name_plural = "Bookings"
       ordering = ["start_time"]
