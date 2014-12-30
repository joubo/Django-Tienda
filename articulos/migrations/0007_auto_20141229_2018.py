# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0006_auto_20141229_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(default=b'', unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(default=b'', unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='nombre',
            field=models.CharField(default=b'', unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
