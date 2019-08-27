from django.contrib import admin

from .models import ExpenseTypes, ProjectExpenses


admin.site.register(ExpenseTypes)
admin.site.register(ProjectExpenses)
