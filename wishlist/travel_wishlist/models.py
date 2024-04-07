from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

class Place(models.Model):
    user = models.ForeignKey('auth.user', null=False, on_delete=models.CASCADE) # on_delete, what happens when the user itself is deleted? || CASCADE == delete all associated places
    name = models.CharField(max_length=200) # char limit
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True) # no limit
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # this is a database query!
        old_place = Place.objects.filter(pk=self.pk).first()
        if old_place and old_place.photo:
            if old_place != self.photo:
                self.delete_photo(old_place.photo)
        
        super().save(*args, **kwargs)

    def delete_photo(self, photo):
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)
    
    def delete(self, *args, **kwargs):
        if self.photo:
            self.delete_photo(self.photo)

        super().delete(*args, **kwargs)

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'
        notes_str = self.notes[100:] if self.notes else 'no notes' # Limit to first 100 characters
        return f'{self.name} visited? {self.visited} on {self.date_visited}. Photo: {photo_str}. Notes: {notes_str}.' # Not for display to user, debugging only
        
