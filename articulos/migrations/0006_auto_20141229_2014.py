# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_auto_20141229_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(related_name='art_cat', default=b'', to='articulos.Categoria'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='descuento',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='fabricante',
            field=models.ForeignKey(related_name='art_fab', default=b'', to='articulos.Fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(default=b'', unique=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='precio',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(default=b'', unique=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fabricante',
            name='nombre',
            field=models.CharField(default=b'', unique=True, max_length=15),
            preserve_default=True,
        ),
    ]
