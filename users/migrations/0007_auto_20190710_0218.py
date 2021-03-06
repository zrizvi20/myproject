# Generated by Django 2.2.1 on 2019-07-09 22:18

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190618_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='client',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='client',
            name='bank_account_no_1',
        ),
        migrations.RemoveField(
            model_name='client',
            name='bank_account_no_2',
        ),
        migrations.RemoveField(
            model_name='client',
            name='bank_name_1',
        ),
        migrations.RemoveField(
            model_name='client',
            name='bank_name_2',
        ),
        migrations.RemoveField(
            model_name='client',
            name='city',
        ),
        migrations.RemoveField(
            model_name='client',
            name='country',
        ),
        migrations.RemoveField(
            model_name='client',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='client',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='client',
            name='landline_no',
        ),
        migrations.RemoveField(
            model_name='client',
            name='mobile_no_1',
        ),
        migrations.RemoveField(
            model_name='client',
            name='mobile_no_2',
        ),
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='national_id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='po_box_no',
        ),
        migrations.RemoveField(
            model_name='client',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='client',
            name='region',
        ),
        migrations.RemoveField(
            model_name='client',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='bank_account_no_1',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='bank_account_no_2',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='bank_name_1',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='bank_name_2',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='city',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='country',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='landline_no',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='mobile_no_1',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='mobile_no_2',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='national_id',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='po_box_no',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='region',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='bank_account_no_1',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='bank_account_no_2',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='bank_name_1',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='bank_name_2',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='city',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='country',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='landline_no',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='mobile_no_1',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='mobile_no_2',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='national_id',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='po_box_no',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='region',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='user',
            name='address_1',
            field=models.CharField(max_length=150, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='address_2',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Address (#2)'),
        ),
        migrations.AddField(
            model_name='user',
            name='bank_account_no_1',
            field=models.CharField(default=None, max_length=150, null=True, verbose_name='Bank account number'),
        ),
        migrations.AddField(
            model_name='user',
            name='bank_account_no_2',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Bank account number (#2)'),
        ),
        migrations.AddField(
            model_name='user',
            name='bank_name_1',
            field=models.CharField(max_length=150, null=True, verbose_name='Bank name'),
        ),
        migrations.AddField(
            model_name='user',
            name='bank_name_2',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Bank name (#2)'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=150, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='landline_no',
            field=models.IntegerField(default=None, null=True, verbose_name='Landline number'),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_no_1',
            field=models.IntegerField(default=None, null=True, verbose_name='Mobile number'),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_no_2',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Mobile number (#2)'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=150, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='user',
            name='national_id',
            field=models.IntegerField(default=None, null=True, verbose_name='National I.D'),
        ),
        migrations.AddField(
            model_name='user',
            name='po_box_no',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='P.O. Box no'),
        ),
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(max_length=150, null=True, verbose_name='Postal code'),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='ZIP Code'),
        ),
    ]
