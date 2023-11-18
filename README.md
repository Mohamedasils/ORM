# Ex02 Django ORM Web Application
## Date:18/10/2023 

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import Football_player,Football_playerAdmin
admin.site.register(Football_player,Football_playerAdmin)

model.py
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
    

```
## OUTPUT
![Screenshot (2)](https://github.com/Mohamedasils/ORM/assets/144870445/2dd9a9ba-89b9-4cdf-bdbc-14c135bfb88a)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully.
