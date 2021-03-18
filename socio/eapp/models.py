from django.db import models
from django.contrib import auth
import datetime
from django.utils import timezone
# Create your models here.
class friend(models.Model):
    user1=models.ForeignKey(auth.models.User,related_name='User1',on_delete=models.CASCADE)
    fri1=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)

class chat(models.Model):
    user=models.ForeignKey(auth.models.User,related_name='User',on_delete=models.CASCADE)
    fri3=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    msg=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    photo=models.ImageField(null=True,blank=True,upload_to='photos/')
    profession=models.CharField(max_length=256,null=True,blank=True)
    city=models.CharField(max_length=256,null=True,blank=True)
    country=models.CharField(max_length=256,null=True,blank=True)
    work_at=models.CharField(max_length=256,null=True,blank=True)
    #ispic=models.BooleanField(default=False)
    #625923325335-87uvs83os1g706idk3563p4vgv5hqc0p.apps.googleusercontent.com
    #soiP3KaTkc3Axr5CpwpuFQLN
class web(models.Model):
    personal_website=models.URLField(null=True,blank=True)
    Insta_Username=models.CharField(max_length=256,null=True,blank=True)
    Twitter=models.CharField(max_length=256,null=True,blank=True)
    Facebook=models.CharField(max_length=256,null=True,blank=True)
    Github=models.URLField(null=True,blank=True)

class post(models.Model):
    owner=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    #like=models.PositiveIntegerField(default=0)
    #comments=models.TextField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True,upload_to='photos/')
    #time=models.DateTimeField(auto_now_add=True,default="")
    caption=models.TextField()
