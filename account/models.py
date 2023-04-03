from django.db import models

from django.contrib.auth.models import User

class UserOTP(models.Model):
    otp = models.CharField(max_length=6,null=True,blank=True)
    fk_user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
