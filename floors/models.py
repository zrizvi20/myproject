from django.db import models

class ProjectFloors(models.Model):
    floor_id = models.AutoField(primary_key=True)
    BASEMENT = 'basement'
    GROUND = 'ground'
    FIRST_FLOOR = 'first'
    SEC_FLOOR = 'second'
    floor_levels = (
        (BASEMENT, 'basement'),
        (GROUND, 'ground'),
        (FIRST_FLOOR, 'first floor'),
        (SEC_FLOOR, 'second floor'),
        )
    floor_name = models.CharField(
        max_length=150,
        choices=floor_levels,
        default=GROUND,
        verbose_name = 'Floor Level'
        )
    floor_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Floor Description')
    floor_covered_area = models.IntegerField(verbose_name = 'Floor Covered Area')
    covered_area_units = models.ForeignKey('units.CoveredAreaUnits', on_delete=models.CASCADE, verbose_name = 'Covered Area Unit')
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, verbose_name = 'Project')

    def __str__(self):
        return self.floor_name

    class Meta:
        verbose_name = 'Project Floors'
        verbose_name_plural = 'Project Floors'
