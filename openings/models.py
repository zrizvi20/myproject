from django.db import models

# Create your models here.


class OpeningTypes(models.Model):
    opening_type_id = models.AutoField(primary_key=True)
    DOOR = 'door'
    WINDOW = 'window'
    VENT = 'ventilation'
    opening_type_names = (
        (DOOR, 'door'),
        (WINDOW, 'window'),
        (VENT, 'ventilation'),
        )
    opening_type_name = models.CharField(
        max_length=150,
        choices=opening_type_names,
        default=DOOR,
        verbose_name = 'Opening Type'
        )
    opening_type_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Opening Description')
    opening_type_desc_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Opening Description')

    def __str__(self):
        return self.opening_type_name

    class Meta:
        verbose_name = 'Opening Types'
        verbose_name_plural = 'Opening Types'


class Openings(models.Model):
    opening_id = models.AutoField(primary_key=True)
    opening_name = models.CharField(max_length=150, verbose_name = 'Opening Name')
    opening_desc_1 = models.CharField(max_length=150, blank=True, verbose_name = 'Opening Description')
    opening_desc_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Opening Description')
    opening_desc_3 = models.CharField(max_length=150, blank=True, verbose_name = 'Opening Description')
    opening_type = models.ForeignKey(OpeningTypes, on_delete=models.CASCADE, verbose_name = 'Opening Type')
    opening_length = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Opening Length')
    opening_width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Opening Width')
    length_unit = models.ForeignKey('units.LengthUnits', on_delete=models.CASCADE, verbose_name = 'Length Unit')
    room_side = models.ForeignKey('rooms.RoomSides', on_delete=models.CASCADE, verbose_name = 'Room Side')

    def __str__(self):
        return self.opening_name
    
    class Meta:
        verbose_name = 'Openings'
        verbose_name_plural = 'Openings'

