from django.contrib import admin

from .models import *

# Register your models here.

myModels= [CoveredAreaUnits, PlotAreaUnits, LengthUnits]
admin.site.register(myModels)
