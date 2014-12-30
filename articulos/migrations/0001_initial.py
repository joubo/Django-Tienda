# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(max_length=15)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('descuento', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(unique=True, max_length=15)),
                ('descripcion', models.TextField()),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(related_name='art_cat', to='articulos.Categoria'),
            preserve_default=True,
        ),
    ]
