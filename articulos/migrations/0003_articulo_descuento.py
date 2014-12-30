# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_auto_20141229_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='descuento',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
