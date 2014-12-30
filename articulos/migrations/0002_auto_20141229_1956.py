# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='descuento',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
