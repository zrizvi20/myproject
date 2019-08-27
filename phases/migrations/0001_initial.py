# Generated by Django 2.2.1 on 2019-06-02 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPhases',
            fields=[
                ('phase_id', models.AutoField(primary_key=True, serialize=False)),
                ('phase_name', models.CharField(choices=[('structure', 'structure'), ('finishing', 'finishing')], default='structure', max_length=150, verbose_name='Phase')),
                ('phase_desc_1', models.CharField(blank=True, max_length=150, verbose_name='Phase Description')),
                ('phase_desc_2', models.CharField(blank=True, max_length=150, verbose_name='Phase Description')),
            ],
            options={
                'verbose_name': 'Project Phases',
                'verbose_name_plural': 'Project Phases',
            },
        ),
        migrations.CreateModel(
            name='PhaseActivities',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_name', models.CharField(choices=[('foundation excavation', 'foundation excavation'), ('lean concrete', 'lean concete'), ('door frame fixing', 'door frame fixing'), ('internal plaster', 'internal plaster')], default='foundation excavation', max_length=150, verbose_name='Activity')),
                ('activity_desc_1', models.CharField(blank=True, max_length=150, verbose_name='Activity Description')),
                ('activity_desc_2', models.CharField(blank=True, max_length=150, verbose_name='Activity Description')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phases.ProjectPhases', verbose_name='Phase')),
            ],
            options={
                'verbose_name': 'Phase Activities',
                'verbose_name_plural': 'Phase Activites',
            },
        ),
    ]
