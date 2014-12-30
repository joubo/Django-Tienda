# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0015_auto_20141229_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'/media/categorias/', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
    ]
