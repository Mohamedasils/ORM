from django.db import models
from django.contrib import admin
class Football_player(models.Model):
     Name=models.CharField(max_length=20)
     Dob=models.DateField()
     Height=models.IntegerField()
     Address=models.CharField(max_length=100)
     MobileNo=models.IntegerField()
class Football_playerAdmin(admin.ModelAdmin):
    list_display=["Name","Dob","Height","Address","MobileNo"]
    