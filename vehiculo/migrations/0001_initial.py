# Generated by Django 4.1 on 2022-08-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=6)),
                ('tipo_vehiculo', models.CharField(max_length=20)),
                ('hora_entrada', models.DateTimeField(auto_now_add=True)),
                ('hora_salida', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
