from django.contrib import admin
from users.models import *

# Register your models here.
myModels= [User, Client, Supervisor, Contractor]
admin.site.register(myModels)
