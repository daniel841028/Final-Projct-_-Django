# Generated by Django 3.0.5 on 2020-05-05 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carsharing', '0003_auto_20200424_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driverlist',
            old_name='location',
            new_name='departure',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.AddField(
            model_name='driverlist',
            name='destination',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        )
    ]