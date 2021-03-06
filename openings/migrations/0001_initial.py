# Generated by Django 2.2.1 on 2019-06-02 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '__first__'),
        ('units', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningTypes',
            fields=[
                ('opening_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('opening_type_name', models.CharField(choices=[('door', 'door'), ('window', 'window'), ('ventilation', 'ventilation')], default='door', max_length=150, verbose_name='Opening Type')),
                ('opening_type_desc', models.CharField(blank=True, max_length=150, verbose_name='Opening Description')),
                ('opening_type_desc_2', models.CharField(blank=True, max_length=150, verbose_name='Opening Description')),
            ],
            options={
                'verbose_name': 'Opening Types',
                'verbose_name_plural': 'Opening Types',
            },
        ),
        migrations.CreateModel(
            name='Openings',
            fields=[
                ('opening_id', models.AutoField(primary_key=True, serialize=False)),
                ('opening_name', models.CharField(max_length=150, verbose_name='Opening Name')),
                ('opening_desc_1', models.CharField(blank=True, max_length=150, verbose_name='Opening Description')),
                ('opening_desc_2', models.CharField(blank=True, max_length=150, verbose_name='Opening Description')),
                ('opening_desc_3', models.CharField(blank=True, max_length=150, verbose_name='Opening Description')),
                ('opening_length', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Opening Length')),
                ('opening_width', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Opening Width')),
                ('length_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.LengthUnits', verbose_name='Length Unit')),
                ('opening_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openings.OpeningTypes', verbose_name='Opening Type')),
                ('room_side', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.RoomSides', verbose_name='Room Side')),
            ],
            options={
                'verbose_name': 'Openings',
                'verbose_name_plural': 'Openings',
            },
        ),
    ]
