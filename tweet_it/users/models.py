from distutils.command import upload
from email.mime import image
from email.policy import default
from tkinter.tix import IMAGE
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save()

        img=Image.open(self.image.path)

        if img.height >350 or img.width > 350:
            output_size = (350, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)

