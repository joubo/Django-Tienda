# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_articulo_descuento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(unique=True, max_length=15),
            preserve_default=True,
        ),
    ]
