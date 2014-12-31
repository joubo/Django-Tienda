# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0021_auto_20141230_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'articulos', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'fabricantes', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
    ]
