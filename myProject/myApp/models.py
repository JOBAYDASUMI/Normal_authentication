from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = [
        ('recruiter','recruiter'),
        ('jobseeker','Jobseeker'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    profile_pic=models.ImageField(upload_to="Media/prifile_pic",null=True)
    
    def __str__(self):
        return f"{self.username}"
