# Generated by Django 4.0 on 2022-11-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoDis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidadmodel',
            name='dispo',
            field=models.BooleanField(default=True),
        ),
    ]
