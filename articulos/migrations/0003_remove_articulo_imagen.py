# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_articulo_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='imagen',
        ),
    ]
