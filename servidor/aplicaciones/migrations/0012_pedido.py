# Generated by Django 4.2.1 on 2023-06-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0011_carrito_total_delete_presupuesto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=2000)),
                ('total', models.IntegerField()),
                ('estado', models.CharField(choices=[('Sin enviar', 'Sin enviar'), ('En trancito', 'En trancito'), ('Completado', 'Completado')], max_length=100)),
            ],
        ),
    ]
