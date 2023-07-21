from django.db import models

class Rooms(models.Model):
    room_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, max_length=20)

    class Meta:
        verbose_name_plural = 'Rooms'


    def __str__(self):
        return f'{self.room_name}'