# Generated by Django 3.2.9 on 2022-04-09 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0013_reserve_cancel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve_cancel',
            name='reserve_cancel_status',
            field=models.TextField(default='取消_初始狀態'),
        ),
        migrations.AlterField(
            model_name='reserve_search',
            name='reserve_search_status',
            field=models.TextField(default='搜尋_初始狀態'),
        ),
    ]