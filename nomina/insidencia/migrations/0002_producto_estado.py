# Generated by Django 4.2 on 2024-10-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insidencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('pendiente', 'Pendiente')], default='pendiente', max_length=10),
        ),
    ]