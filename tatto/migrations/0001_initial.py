# Generated by Django 4.0 on 2022-11-16 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tattoo_artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(max_length=150)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('like', models.TextField(max_length=150)),
                ('departament', models.TextField(max_length=150)),
                ('municipio', models.TextField(max_length=150)),
                ('direction', models.TextField(max_length=150)),
                ('experience', models.IntegerField()),
                ('description', models.TextField(max_length=150)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PerfilProfesional', to='accounts.users')),
            ],
        ),
    ]
