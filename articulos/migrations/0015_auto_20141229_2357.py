# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0014_auto_20141229_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'{{MEDIA_URL}}', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
    ]
