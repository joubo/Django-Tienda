# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0007_auto_20141229_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'articulos', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'categorias', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fabricante',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'fabricantes', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
    ]
