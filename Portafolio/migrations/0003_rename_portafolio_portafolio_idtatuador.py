# Generated by Django 4.0 on 2022-11-19 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0002_alter_portafolio_portafolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portafolio',
            old_name='portafolio',
            new_name='idTatuador',
        ),
    ]
