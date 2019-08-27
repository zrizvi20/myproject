from django.contrib import admin
from .models import Country, City, Region
# Register your models here.
my_models = [Country,
             City,
             Region
             ]

admin.site.register(my_models)
