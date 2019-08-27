from django.db import models

# Create your models here.


class ProjectPhases(models.Model):
    phase_id = models.AutoField(primary_key=True)
    STRUCTURE = 'structure'
    FINISHING = 'finishing'
    phase_names = (
        (STRUCTURE, 'structure'),
        (FINISHING, 'finishing'),
        )
    phase_name = models.CharField(
        max_length=150,
        choices=phase_names,
        default=STRUCTURE,
        verbose_name = 'Phase'
        )
    phase_desc_1 = models.CharField(max_length=150, blank=True, verbose_name = 'Phase Description')
    phase_desc_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Phase Description')

    def __str__(self):
        return self.phase_name

    class Meta:
        verbose_name = 'Project Phases'
        verbose_name_plural = 'Project Phases'

class PhaseActivities(models.Model):
    activity_id = models.AutoField(primary_key=True)
    FOUND_EXC = 'foundation excavation'
    LEAN_CONC = 'lean concrete'
    DOOR_F_F = 'door frame fixing'
    INT_PLAST = 'internal plaster'
    activity_names = (
        (FOUND_EXC, 'foundation excavation'),
        (LEAN_CONC, 'lean concete'),
        (DOOR_F_F, 'door frame fixing'),
        (INT_PLAST, 'internal plaster'),
        )
    activity_name = models.CharField(
        max_length=150,
        choices=activity_names,
        default=FOUND_EXC,
        verbose_name = 'Activity'
        )
    activity_desc_1 = models.CharField(max_length=150, blank=True, verbose_name = 'Activity Description')
    activity_desc_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Activity Description')
    phase = models.ForeignKey(ProjectPhases, on_delete=models.CASCADE, verbose_name = 'Phase')

    def __str__(self):
        return self.activity_name

    class Meta:
        verbose_name = 'Phase Activities'
        verbose_name_plural = 'Phase Activites'

