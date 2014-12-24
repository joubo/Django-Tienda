# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login_id', models.CharField(max_length=30)),
                ('nombre', models.CharField(default=b'', max_length=30, blank=True)),
                ('apellidos', models.CharField(default=b'', max_length=30, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
