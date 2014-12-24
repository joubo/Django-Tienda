# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='login_id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=True, unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
