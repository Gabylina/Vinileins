# Generated by Django 4.2.1 on 2023-06-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0015_clipedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipedido',
            name='cliente',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='clipedido',
            name='pedido',
            field=models.CharField(max_length=2000),
        ),
    ]
