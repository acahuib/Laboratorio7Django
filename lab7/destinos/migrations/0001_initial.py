# Generated by Django 5.0.6 on 2024-06-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('fecha_visita', models.DateField()),
            ],
        ),
    ]
