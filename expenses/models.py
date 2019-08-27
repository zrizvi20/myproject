from django.db import models

# Create your models here.

class ExpenseTypes(models.Model):
    expense_type_id = models.AutoField(primary_key=True)
    LABOUR = 'labour'
    MATERIAL = 'material'
    expense_type_names = (
        (LABOUR, 'labour'),
        (MATERIAL, 'material')
        )
    expense_type_name = models.CharField(
        max_length=150,
        choices=expense_type_names,
        default=LABOUR,
        verbose_name = 'Expense Type')
    expense_type_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Expense Type Description')
    expense_type_desc_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Expense Type Description')

    def __str__(self):
        return self.expense_type_name

    class Meta:
        verbose_name = 'Expense Types'
        verbose_name_plural = 'Expense Types'


class ProjectExpenses(models.Model):
    expense_id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=150, verbose_name = 'Expense Name')
    expense_desc = models.CharField(max_length=150, verbose_name = 'Expense Description')
    expense_desc2 = models.CharField(max_length=150, verbose_name = 'Expense Description')
    expense_type = models.ForeignKey(ExpenseTypes, on_delete=models.CASCADE, verbose_name = 'Expense Type')
    expense_value = models.CharField(max_length=150, verbose_name = 'Expense Value')
    project = models.ForeignKey('projects.Project', on_delete = models.CASCADE, verbose_name = 'Project')
    activity = models.ForeignKey('phases.PhaseActivities', on_delete=models.CASCADE, verbose_name = 'Activity')
    phase = models.ForeignKey('phases.ProjectPhases', on_delete=models.CASCADE, verbose_name = 'Phase')
    floor = models.ForeignKey('floors.ProjectFloors', on_delete=models.CASCADE, verbose_name = 'Floor')
    room = models.ForeignKey('rooms.FloorRooms', on_delete=models.CASCADE, verbose_name = 'Room')

    def __str__(self):
        return self.expense_name

    class Meta:
        verbose_name = 'Project Expenses'
        verbose_name_plural = 'Project Expenses'

