# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0004_auto_20141229_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='fabricante',
            name='nombre',
        ),
    ]
