from django.db import models

# Create your models here.

class CoveredAreaUnits(models.Model):
    covered_area_unit_id = models.AutoField(primary_key=True)
    SQUARE_FEET = 'square feet'
    SQUARE_METERS = 'square meters'
    SQUARE_YARDS = 'square yards'
    covered_area_unit_types = (
        (SQUARE_FEET, 'square feet'),
        (SQUARE_METERS, 'square meters'),
        (SQUARE_YARDS, 'square yards')
        )
    covered_area_unit_name = models.CharField(
        max_length=150,
        choices = covered_area_unit_types,
        default = SQUARE_FEET,
        verbose_name = 'Covered Area Unit Name')
    covered_area_unit_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Covered Area Unit Description')

    def __str__(self):
        return self.covered_area_unit_name
    
    class Meta:
        verbose_name = 'Covered Area Units'
        verbose_name_plural = 'Covered Area Units'


class LengthUnits(models.Model):
    length_unit_id = models.AutoField(primary_key=True)
    METERS = 'meters'
    MILLI_MET = 'millimeters'
    CENTI_MET = 'centimeters'
    FEET = 'feet'
    YARDS = 'yards'
    INCHES = 'inches'
    length_unit_names = (
        (METERS, 'meters'),
        (FEET, 'feet'),
        (YARDS, 'yards'),
        (INCHES, 'inches'),
        (MILLI_MET, 'millimeters'),
        (CENTI_MET, 'centimeters'),
        )
    length_unit_name = models.CharField(
        max_length = 150,
        choices = length_unit_names,
        default = METERS,
        verbose_name = 'Length Unit'
        )
    length_unit_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Length Unit Description')

    def __str__(self):
        return self.length_unit_name

    class Meta:
        verbose_name = 'Length Units'
        verbose_name_plural = 'Length Units'


class PlotAreaUnits(models.Model):
    plot_area_unit_id = models.AutoField(primary_key = True)
    SQUARE_FEET = 'square feet'
    SQUARE_METERS = 'square meters'
    SQUARE_YARDS = 'square yards'
    MARLA = 'marla'
    KANAL = 'kanal'
    plot_area_unit_types = (
        (SQUARE_FEET, 'square feet'),
        (SQUARE_METERS, 'square meters'),
        (SQUARE_YARDS, 'square yards'),
        (MARLA, 'marla'),
        (KANAL, 'kanal')
        )
    plot_area_unit_name = models.CharField(
        max_length=150,
        choices = plot_area_unit_types,
        default = SQUARE_FEET,
        verbose_name = 'Plot Area Units')
    plot_area_unit_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Plot Area Unit Description')


    def __str__(self):
        return self.plot_area_unit_name
    
    class Meta:
        verbose_name = 'Plot Area Units'
        verbose_name_plural = 'Plot Area Units'

