# Generated by Django 4.2.4 on 2023-08-28 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='litres_per_day',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6),
        ),
    ]