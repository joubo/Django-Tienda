from django.db import models
from django.contrib.auth.models import User


# Create your models here.

User.add_to_class('dni', models.CharField(max_length=9, null=True)),
User.add_to_class('address', models.CharField(max_length=50, null=True)),
User.add_to_class('phone', models.CharField(max_length=9, null=True)),