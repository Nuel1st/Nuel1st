from django.db import models

# Create your models here.

class UserProfile(models.Model):
    event_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    pincode = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_ID = models.CharField(max_length=100)
    phone_brand = models.CharField(max_length=100)
    voice_ID = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
