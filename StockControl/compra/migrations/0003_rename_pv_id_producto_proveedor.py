# Generated by Django 5.0.3 on 2024-03-26 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_rename_proveedor_producto_pv_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='pv_id',
            new_name='proveedor',
        ),
    ]
