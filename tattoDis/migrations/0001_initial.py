# Generated by Django 4.0 on 2022-11-21 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='disponibilidadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispo', models.TextField(max_length=150)),
                ('iDispo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iDispo', to='accounts.users')),
            ],
        ),
    ]
