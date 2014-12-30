# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0009_auto_20141229_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'/articulos/media/articulos', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
    ]
