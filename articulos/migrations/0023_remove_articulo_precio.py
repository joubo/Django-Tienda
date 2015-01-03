# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0022_auto_20141230_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='precio',
        ),
    ]
