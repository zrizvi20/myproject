from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = CountryField(verbose_name = 'Country Name')
    country_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Country Description')

    def __str__(self):
        return str(self.country_name)
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=100, verbose_name = 'Region Name')
    region_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Region Description')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name = 'Country')
    
    def __str__(self):
        return self.region_name
    
    class Meta:
        verbose_name = 'Region'
    
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50, verbose_name = 'City Name')
    city_desc = models.CharField(max_length=150, blank=True, verbose_name = 'City Description')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name = 'Region')

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
