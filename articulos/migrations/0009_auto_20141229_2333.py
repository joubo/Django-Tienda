# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0008_auto_20141229_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'articulos/media/articulos', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
    ]
