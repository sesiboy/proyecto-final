# Generated by Django 5.1.2 on 2024-12-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('cantidad_disponible', models.IntegerField()),
                ('fecha_vencimiento', models.DateField()),
                ('id_distribuidor', models.IntegerField()),
            ],
        ),
    ]
