from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    user = models.ForeignKey('auth.user', null=False, on_delete=models.CASCADE) # CASCADE == delete all associated places
    name = models.CharField(max_length=200) # char limit
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images', blank=True, null=True)

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'
        notes_str = self.notes[100:] if self.notes else 'no notes' # Limit to first 100 characters
        return f'{self.name} visited? {self.visited} on {self.date_visited}. Photo: {photo_str}. Notes: {notes_str}.' # Not for display to user, debugging only
        
