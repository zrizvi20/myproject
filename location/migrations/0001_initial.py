# Generated by Django 2.2.1 on 2019-06-02 16:27

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', django_countries.fields.CountryField(max_length=2, verbose_name='Country Name')),
                ('country_desc', models.CharField(blank=True, max_length=150, verbose_name='Country Description')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(max_length=100, verbose_name='Region Name')),
                ('region_desc', models.CharField(blank=True, max_length=150, verbose_name='Region Description')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Region',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50, verbose_name='City Name')),
                ('city_desc', models.CharField(blank=True, max_length=150, verbose_name='City Description')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Region', verbose_name='Region')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
