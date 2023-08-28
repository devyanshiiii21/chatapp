from django.db import models
from django.contrib.auth.models import User

class Rooms(models.Model):
    room_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, max_length=20)

    class Meta:
        verbose_name_plural = 'Rooms'


    def __str__(self):
        return f'{self.room_name}'
    

class Message(models.Model):
    room = models.ForeignKey(Rooms, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)