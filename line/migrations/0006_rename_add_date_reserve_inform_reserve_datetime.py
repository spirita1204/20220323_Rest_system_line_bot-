# Generated by Django 3.2.9 on 2022-04-03 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0005_reserve_inform_add_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserve_inform',
            old_name='add_date',
            new_name='reserve_datetime',
        ),
    ]