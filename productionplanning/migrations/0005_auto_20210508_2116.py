# Generated by Django 3.1.7 on 2021-05-08 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionplanning', '0004_auto_20210508_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacityscheduling',
            name='AvalMcOrResHour',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='AVAL MC/RES HOUR'),
        ),
        migrations.AlterField(
            model_name='capacityscheduling',
            name='ReqdMcOrResHour',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='REQD MC/RES HOUR'),
        ),
    ]
