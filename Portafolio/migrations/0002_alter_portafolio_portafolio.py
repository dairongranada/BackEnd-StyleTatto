# Generated by Django 4.0 on 2022-11-19 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('Portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='portafolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IdTatuador', to='accounts.users'),
        ),
    ]