# Generated by Django 4.2.4 on 2023-08-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_litresbeforenexttopup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='litres_per_day',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
