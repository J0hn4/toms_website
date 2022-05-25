from django.db import models
from django.utils import timezone

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(blank=True, null=True, upload_to='announcements/images/')
    content = models.TextField()

    def __str__(self):
        return self.title