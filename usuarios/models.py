from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#User.add_to_class('username',  models.CharField(max_length=30, unique = True),
#User.add_to_class('firsname', models.CharField(max_length=30, blank=True, default=''),
#User.add_to_class('lastname', models.CharField(max_length=30, blank=True, default=''),
#User.add_to_class('email', models.EmailField(),
#User.add_to_class('password', models.CharField(max_length=20),
User.add_to_class('dni', models.CharField(max_length=9, null=True)),
User.add_to_class('address', models.CharField(max_length=50, null=True)),
User.add_to_class('phone', models.CharField(max_length=9, null=True)),