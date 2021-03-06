# Generated by Django 2.2.1 on 2019-06-18 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190618_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
        migrations.RemoveField(
            model_name='client',
            name='username',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='username',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='username',
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contractor',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
